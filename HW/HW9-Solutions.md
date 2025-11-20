---
---

# HW 9 Solutions

* Table of Contents
{:toc}

[HW 9 Questions](HW9)



## (1) Golden Section Search

### (1.1) Working out by hand

<embed src="GoldenSectionSearchCompleted.pdf" width="500" height="375" 
 type="application/pdf">

### (1.2) Pseudo-code

Consider the following procedure.

```
Given: a,b,epsilon, and the function f to be maximized
R = (sqrt(5)-1)/2
h = b-a
x1 = b - R*h
x2 = a + R*h
f1 = f(x1)
f2 = f(x2)
while h > epsilon:
	if f1 > f2:
		leave a unchanged
		change b to be the current value of x2
		update h = b-a
		change x2,f2 to be the current value of x1,f1
		update x1 = b - R*h
		calculate a new f1 = f(x1)
	else if f1 < f2:
		change a to be the current value of x1
		leave b unchanged
		update h = b-a
		change x1,f1 to be the current value of x2,f2
		update x2 = a + R*h
		calculate a new f2 = f(x2)
once the loop has exited because h became smaller than epsilon,
return (a+b)/2
```

...

## (2) Naive multi-dimensional optimization

<embed src="NaiveNdimOpt.pdf" width="500" height="375" 
 type="application/pdf">




{% include mathjax.html %}
