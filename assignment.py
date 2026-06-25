# prime no
# def prime_no(num):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return True
# numbers=[2,5,10,19,18]
# for n in numbers:
#     if prime_no(n):
#         print(n,"is prime")
#     else:
#         print(n,"not prime")

#Fibonacci
# def fibonacci(num):
#     a-0
#     b=1
#     for i in range(num):
#         print(a)
#         a,b=b,a+b
# fibonacci(8)    

#palindrome
# def palindrome(value):
#     value=str(value)
#     if value == value[::-1]:
#         print(value,"value is palindrome")
#     else:
#         print(value,"value is not palindrome")
# palindrome(121)

#armstrong
# def armstrong(num):
#     power=len(str(num))
#     total=0

#     for digit in str(num):
#         total+=int(digit) ** power
    
#     if total==num:
#         print(num,"is armstrong")
#     else:
#         print(num,"is not armstrong")
# armstrong(321)
# armstrong(153)
# armstrong(345)


#lambda functions
square=lambda x:x*x
cube=lambda x:x*x*x
maximum=lambda a,b: a if a>b else b
even_odd=lambda n:"Even" if n%2==0 else "Odd"
c_to_f=lambda c:(c*9/5) + 32

print("square:",square(2))
print("cube:",cube(2))
print("maximum:",maximum(9,2))
print("even_odd:",even_odd(2))
print("c_to_f:",c_to_f(4))