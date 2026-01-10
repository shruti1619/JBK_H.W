def addTwo(a,b):
    """
    input: we take two args for addition numbers
    return: returning the addition of two numbers
    """
    return a+b

print(addTwo.__doc__)

import math
def area_circle(radius):
    """calculating area of circle given its radius
       input: radius(float) to perform area of circle 
       result:return(float) to return area of circle """
       
    return math.pi*radius**2

print(area_circle.__doc__)