#code 6 ; write a program to swap two numbers using a third variable
num1=58
num2=90
num3=num1 #will have 58
num1=num2 #will have 90
num2=num3 #will have 58
print("after swaping first number is:",num1)
print("after swaping second number is:",num2)

#code 7 : same progran but without using third variable
xnum=77
ynum=88
xnum,ynum=ynum,xnum
print("Now first num is:",xnum)
print("Now second num is:",ynum)

#code 8 ; celcius to fahrenheight converter
celcius=float(input("Enter temp in degree celcius:"))
fahrenheight=(celcius*9/5)+32
print("The temperatue in fahrenheight is:",fahrenheight)

#code 9 ; program to read total and average marks of five subjects
maths=float(input("enter marks of maths:"))
science=float(input("enter marks of science:"))
physics=float(input("enter marks of physics:"))
chemistry=float(input("enter marks of chemistry:"))
english=float(input("enter marks of english:"))
total=maths+science+physics+chemistry+english
avg=total/5
print("total marks are:",total,"average marks are:",avg)

#code 10; convert seconds into time in hours,minutes and seconds;

sec=int(input("enter the time in seconds:"))
hours=sec//3600
minutes=(sec%3600)//60
sec2=sec%60
print("The time is",hours,"hours:",minutes,"minutes:",sec2,"seconds")




