# Takes as input a list of numbers and returns a single number
# equal to the standard deviation of the list of numbers given.
def std(data):
    # Step 1: Calculate the mean
    mean = sum(data) / len(data)
    
    # Step 2: Calculate the squared differences from the mean
    squared_diffs = [(x - mean) ** 2 for x in data]
    
    # Step 3: Calculate the variance (mean of squared differences)
    variance = sum(squared_diffs) / len(data)
    
    # Step 4: Standard deviation is the square root of variance
    std_dev = variance ** 0.5
    
    return std_dev

def magnitude(a,b,c):
    # Use 3-d Pythagorean theorem to calculate magnitude of
    # a vector with three components a, b and c
    return (a**2 + b**2 + c**2)**(1/2)
