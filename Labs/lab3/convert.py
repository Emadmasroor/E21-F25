import svgelements
import sys
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_MIN = np.array([30, -50])
OUTPUT_MAX = np.array([80, 50])

OUTPUT_DIMS = OUTPUT_MAX - OUTPUT_MIN
OUTPUT_MID = 0.5*(OUTPUT_MIN + OUTPUT_MAX)

MIN_FEATURE_SIZE_MM = 3.0

class SvgTransformer:

    def __init__(self, width, height, scl):

        self.scl = scl
        self.dims = np.array([width, height], dtype=np.float32) * scl

        shift = np.array([[1, 0, 0],
                             [0, 1, self.dims[1]],
                             [0, 0, 1]])
        
        flip = np.array([[1, 0, 0],
                            [0, -1, 0],
                            [0, 0, 1]])

        S = np.array([[scl, 0, 0],
                         [0, scl, 0],
                         [0, 0, 1]])

        self.global_transform = np.dot(np.dot(shift, flip), S)
        

        self.local_transform = np.eye(3)

    def set_local_transform(self, xx, yx, xy, yy, x0, y0):

        self.local_transform = np.array([[xx, xy, x0],
                                            [yx, yy, y0],
                                            [0, 0, 1]])

    def transform(self, x, y):

        point = np.array([x, y, 1])
        point = np.dot(self.local_transform, point)
        point = np.dot(self.global_transform, point)

        return point[:2].astype(np.float32)

    def scale_dims(self, x, y):
        return self.scl * x, self.scl*y

######################################################################
# helper function for below

def _flatten(seg, scl, u0, p0, u1, p1, points):

    # precondition: points[-1] = p0 unless very first point

    d01 = svgelements.Point.distance(p0, p1)

    if d01*scl > MIN_FEATURE_SIZE_MM:

        umid = 0.5*(u0 + u1)
        pmid = seg.point(umid)

        _flatten(seg, scl, u0, p0, umid, pmid, points)

        # now pmid is added

        _flatten(seg, scl, umid, pmid, u1, p1, points)

        # now p1 is added

    else:

        points.append(p1)

    # postcondition: points[-1] = p1

######################################################################
# flatten a bezier path segment
    
def flatten(seg, scl):
    
    p0 = seg.point(0)
    p1 = seg.point(1)

    points = []
    
    _flatten(seg, scl, 0.0, p0, 1.0, p1, points)

    return points

######################################################################

def main():

    svg = svgelements.SVG.parse(sys.argv[1], color='none')
    outfile = open(sys.argv[2], 'w')

    input_dims = np.array([svg.viewbox.width, svg.viewbox.height])
    scl = (OUTPUT_DIMS / input_dims).min()

    print('scl is', scl)


    xform = SvgTransformer(svg.viewbox.width,
                           svg.viewbox.height, scl)

    items = [ item for item in svg ]

    contours = []

    while len(items):

        item = items.pop(0)

        if isinstance(item, svgelements.Group):
            items = [ child for child in item ] + items
            continue

        # any geometry we want to deal with has an xform
        if not hasattr(item, 'transform'):
            continue

        xx, yx, xy, yy, x0, y0 = [getattr(item.transform, letter)
                                  for letter in 'abcdef']

        det = xx*yy - yx*xy
        is_rigid = (abs(det - 1) < 1e-4)

        assert(is_rigid)

        xform.set_local_transform(xx, yx, xy, yy, x0, y0)

        points = None
        is_closed = False

        if isinstance(item, svgelements.Rect):

            w, h = xform.scale_dims(item.width, item.height)

            cx = item.x + 0.5*item.width
            cy = item.y + 0.5*item.height

            p0 = xform.transform(item.x, item.y)
            p1 = xform.transform(item.x + item.width, item.y)
            p2 = xform.transform(item.x + item.width, item.y + item.height)
            p3 = xform.transform(item.x, item.y + item.height)

            points = np.array([p0, p1, p2, p3])
            is_closed = True

        elif (isinstance(item, svgelements.Circle) or
              isinstance(item, svgelements.Ellipse)):

            ctr = xform.transform(item.cx, item.cy)

            print("TODO: CIRCLE!!!")

        elif isinstance(item, svgelements.SimpleLine):

            p0 = xform.transform(item.x1, item.y1)
            p1 = xform.transform(item.x2, item.y2)

            points = np.array([p0, p1])
            is_closed = False

        elif isinstance(item, svgelements.Polyline):

            points = np.array(
                [xform.transform(p.x, p.y) for p in item.points])

            is_closed = False

        elif isinstance(item, svgelements.Path):

            points = []

            for seg in item.segments():
                if isinstance(seg, svgelements.Move):
                    if points:
                        points = np.array([ xform.transform(p.x, p.y) for p in points ])
                        if is_closed:
                            points = np.vstack([points, [points[0]]])
                        contours.append(points)
                        points = []
                    points.append(seg.point(0))
                elif isinstance(seg, svgelements.Line):
                    points.append(seg.point(1))
                elif isinstance(seg, svgelements.Close):
                    is_closed = True
                else:
                    points.extend(flatten(seg, scl))

            points = np.array([ xform.transform(p.x, p.y) for p in points ])

        elif isinstance(item, svgelements.Polygon):

            points = np.array(
                [xform.transform(p.x, p.y) for p in item.points])

            is_closed = True

        else:

            print('*** warning: ignoring SVG item:', item, '***')
            continue

        if points is not None:
            if is_closed:
                points = np.vstack([points, [points[0]]])

            contours.append(points)

    '''
    svg = svgelements.SVG.parse(sys.argv[1])

    outfile = open(sys.argv[2], 'w')
    
    contours = []
    
    for element in svg.elements():

        if isinstance(element, svgelements.SVG):
            pass
        elif isinstance(element, svgelements.Group):
            pass
        elif isinstance(element, svgelements.Path):

            contour = []
            
            for i, item in enumerate(element):
                if isinstance(item, svgelements.Move):
                    if len(contour):
                        contours.append(contour)
                        contour = []
                    contour.append(tuple(item.end))
                elif isinstance(item, svgelements.Line):
                    assert(contour[-1] == tuple(item.start))
                    contour.append(tuple(item.end))
                elif isinstance(item, svgelements.Close):
                    contour.append(contour[0])
                    contours.append(contour)
                    contour = []
                else:
                    raise RuntimeError('unsupported item type:', type(item))

            if len(contour):
                contours.append(contour)

        else:
            raise RuntimeError('unsupported element type:', type(element))
    '''

    all_points = np.vstack(contours)

    cmin = all_points.min(axis=0)
    cmax = all_points.max(axis=0)

    cmid = 0.5*(cmin + cmax)
    cdims = cmax - cmin

    scl = (OUTPUT_DIMS / cdims).min()
    
    for i, contour in enumerate(contours):

        contour -= cmid
        contour *= (scl, scl)
        contour += OUTPUT_MID

        if i > 0:
            print(file=outfile)
        
        for x, y in contour:
            print(x, y, file=outfile)

    for contour in contours:
        plt.plot(contour[:,0], contour[:,1], '.-')

    plt.axis('equal')
    plt.show()


######################################################################

main()

