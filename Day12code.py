# code 56; Write a program to find the LCM of two numbers
import math
num1=int(input("Enter number 1st:"))
num2=int(input("Enter number 2nd:"))
result=math.lcm(num1,num2)
print(f"The LCM of{num1} and{num2} is {result}",)



#SERIES AND PATTERNS
#code 57 ; Write a program to display the first n terms of the Fibonacci series.
a=0
b=1
c=0
num_1=int(input("Enter number of fibanacci terms you want : "))
for i in range(0,num_1):
        print(a)
        c=a+b
        a=b
        b=c



#code 58 ;  Write a program to find the sum of the first n terms of the Fibonacci series.      
d=0
e=1
f=0
sum=0
num_2=int(input("Enter number of sum of fibanacci terms you want: "))
for j in range(0,num_2):
        print(d)
        sum+=d
        f=d+e
        d=e
        e=f
print("sum is:",sum)



#code 59; Write a program to find the sum of the series 1 + 2 + 3 + ... + n.
n=int(input("Enter no. to find sum of natural sumbers till there:"))
naturalsum=0
for k in range(1,n+1):
    naturalsum+=k
    print(k)    
print(f"the sum of natural numbers till{n} is: {naturalsum}")  



#code 60 ; Write a program to find the sum of the series 1^2 + 2^2 + 3^2 + ... + n^2.
series=int(input("Enter no. to find sum of natural sumbers till there:"))
squaresum=0
square=1
for l in range(1,series+1):
    square=l*l
    print(square)
    squaresum+=square
print(f"the sum of natural numbers till{series} is: {squaresum}")  
