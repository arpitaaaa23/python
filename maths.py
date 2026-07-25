import numpy as np
arr=np.array([1,1,2,4])
print(arr)

arr1 = np.zeros(5)
print(arr1)

arr2 = np.zeros(5)
print(arr2)

arr3 = np.zeros((2,3))
print(arr3)

arr4 = np.full(5,10)
print(arr4)

arr5 = np.arange(1,11)
print(arr5)

arr6 = np.linspace(1,10,5)
print(arr6)

arr7 = np.random.randint(1,200,10)
print(arr7)

arr8 = np.arange(1,13)
print(arr8)

arr9 = arr8.reshape(3,4)
print(arr9)

a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(np.sqrt(a))
print(np.sqrt(b))
print(np.sqrt(a+b))
print(np.abs(a))
print(a+5)
b=[2,4,6,8]
b.append(2)
print(b)
c=[]
for i in b:
    c.append(i*2)
print(c)
d=np.array([1,2,3,4,5,6])
print(d*5)




