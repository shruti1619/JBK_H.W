import numpy

l=[10,20.5,30,40,50,60]
ar=numpy.array(l)
print(ar)

#0D array
ar0=numpy.array(40)
print(ar0)

#1D array
ar1=numpy.array([10,20,30,40,50])
print(ar1)
"""it is collection of elements in a single line."""

print()
#2D array
ar2=numpy.array([[10,20,30],[40,50,60]])
print(ar2)
'''
It is collection of 1D arrays.
this is two diementional array which must be in the form of rows and columns and number of columns in each row must be same.but row can be of any number For example:
[
    [10 20 30]
    [40 50 60]
 ]
 '''
print()
#3D array
ar3=numpy.array([[[10,20],[30,40]],[[50,60],[70,80]]])
print(ar3)

'''
It is collection of 2D arrays.
this is three dimensional array which must be in the form of layers, rows and columns and number of rows and columns in each layer must be same.but layers can be of any number.For example:
[   
    [
        [10 20]
        [30 40] 
    ]
    [
        [50 60]
        [70 80]
    ]
]
'''

''' 
properties/Atribute of numpy array
#1.ndim - it shows the dimension of array
'''
ar1=numpy.array([10,20,30,40,50])
ar2=numpy.array([[10,20,30],[40,50,60]])
print(ar1.ndim)
print(ar2.ndim)
print(ar3.ndim)

#2. Size - it shows the total number of elements in the array
print(ar1.size)
print(ar3.size)

#3. Shape - it shows the number of elements in each dimension
print(ar1.shape)
print(ar2.shape)
print(ar3.shape)

#4. dtype - it shows the data type of elements in the array
print(ar1.dtype)

'''
Creating numpy arrays using built-in functions
'''
import numpy as np
# zeros function
a=np.zeros((4,))
b=np.zeros((3,4))
print(a,'\n')
print(b,'\n')

# ones function give ones array but dtype is float by default
c=np.ones((4,))
d=np.ones((4,3))
print(c,'\n')
print(d,'\n')

# full function it is used to create array of any number we want
a1=np.full((3,),5)
a2=np.full((4,3),7)
print(a1,'\n')
print(a2,'\n')

# arange function it is like range function of python but it returns array
a3=np.arange(1,11,1)
print(a3)

a4=np.arange(5,51,5)
print(a4)
a5=np.arange(8)
print(a5)

# reshape function it is used to change the shape of array without changing its data 
a6=np.reshape(a3,(5,2))
a7=a4.reshape(2,5)
a8=a5.reshape(2,2,2)
print(a6,'\n')
print(a7, '\n')
print(a8, '\n')

print(ar2.reshape(6,))

ar1=np.array([10,20,30,40,50])
print(ar1)
print(ar1+2)
print(ar1/5)
print(ar1*2)
print(ar1**2)


