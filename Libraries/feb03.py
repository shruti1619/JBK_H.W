import numpy as np


ar2=np.array([[10,20,30],[40,50,60]])
print(ar2)
print(ar2[0])
print(ar2[0][-1])
print(ar2[0,-1])
print(ar2[1,1])
print(ar2[-1][-2])

ar1=np.array([10,20,30,40,50])
print(ar1[1::1])
print(ar1[-1:1:-1])

print(ar2[0,1:-1])

ar3=np.array([[[10,20,30],[40,50,60]],[[70,80,90],[100,110,120]]])
print(ar3)

print(ar3[0][0,0:2])
# print(ar3[3,1,0:2])
print(ar3[0:-1,0])
print(ar3[0:-1,0:3])

ar1=np.array([10,20,30,40,50,11])
print(np.sum(ar1))
print(np.average(ar1))
print(np.min(ar1))
print(np.max(ar1))
print(np.std(ar1))
print(np.var(ar1))

ar=np.array([60,70,80,90,100])
print(np.concatenate((ar1,ar)) )

print()
ar2=np.array([[10,20,30],[40,50,60]])
ar4=np.array([[70,80,90],[100,110,120]])
print(ar2,'\n\n',ar4,'\n')
arr=np.concatenate((ar2,ar4),axis=0)
print( arr )
print()
print( np.concatenate((ar2,ar4),axis=1) )

a=np.vstack((ar2,ar4))
print(a)
b=np.hstack((ar2,ar4))
print(b)

print(np.split(ar1,2))
print(np.split(ar4,2))
print(np.split(ar3,2,axis=1))


p=np.array([11,22,33,44,55])
q=np.array([66,77,88,99,110])
r=np.array([[12,13,14,15],[16,17,18,19],[20,21,22,23]])
print(np.hstack((p,q)))  #[11 22 33 44 55 66 77 88 99 110]
#print(np.concatenate((r,p))) # it will give error because shapes are not compatible for concatenation

x=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.where(x>5))
print(np.where(x%2!=0))
print(np.where(x%2==0, 'even','odd'))
print(np.sort(x))
print(np.ravel(x))             #it returns the flattened array as a view if possible (it means changes made in #                               ravelled array will affect original array)
flattened_array = x.flatten()  #it creates a copy of the array changes made in flattened_array will not affect x
print(flattened_array)

