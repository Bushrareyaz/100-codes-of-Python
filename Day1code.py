#Level 1 — (Output, variables, basic input)

#1ST CODE; Baic print statement in python
print("Hello world")

#2nd code; program to calculate Sum of two numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum=num1+num2
print("The sum of two numbers are:",sum)

#3rd code; program to calculate the sum,subtraction,multiplication and division of two numbers
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
Sum=x+y
subtr=y-x
product=x*y
quot=y/x
print("The addition of two numbers are:",Sum)
print("The subtraction of two numbers are:",subtr)
print("The multiplication of two numbers are:",product)
print("The quotient of two numbers are:",quot)

#4th code; program to calculate radius,area and circumference of circle
radius=int(input("Enter radius of circle:"))
Area1=3.14*radius*radius
Circum=2*3.14*radius
print("The area of circle is:",Area1)
print("The circumference of circle is:",Circum)

#5th code; program to calculate length, breadth, area and perimeter of rectangle
length=int(input("Enter length of rectangle:"))
breadth=int(input("Enter breadth of rectangle:"))
Area2=length*breadth
perim=2*(length+breadth)
if length==breadth:
    print("The shape is a square:")
print("The area of rectangle is:",Area2)
print("The perimeter of rectangle is:",perim)
