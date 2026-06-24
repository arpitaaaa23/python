add=lambda a,b:a+b
print(add(10,20))

square=lambda a,b:a*b
print(square(14,10))

#lambda with map()
numbers=[1,2,3,4,5]
squares=list(map(lambda x:x*x,numbers))
print(squares)

#lambda with filter
numbers=[10,15,20,25,30]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

#lambda fun cube of no
cube=lambda x:x**3
for i in range(5):
    num = int(input("enter no:"))
    print("cube:",cube(num))

