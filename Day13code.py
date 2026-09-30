#code 61 ;Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.
n=int(input("Enter value of n of series 1/n till there:"))
sum=0
for k in range(1,n+1):
    sum+=1/k    
print(f"the sum of series of 1/n till{n} is: {sum}")  


#code 62 ;Write a program to find the value of x raised to the power y without using inbuilt power.
num_1=int(input("Enter value of x:"))
num_2=int(input("Enter value of y:"))
result=num_1**num_2
print("result is",result)    



#code 63 ;Write a program to print a right-angled triangle pattern of stars of height n.
rows=int(input("no. of rows in stars:"))
for i in range(1,rows+1):
    for j in range(1,i+1):#i=1,1+1=2,range=(1,2)
        print("*",end=" ")
    print()  



#code 64 ; Write a program to print an inverted right-angled triangle pattern of stars of height n.
inverse=int(input("Enter rows of inverted stars:"))
for k in range(inverse,0,-1):
    for l in range(k):
       print("*",end=" ")
    print()



#code 65 ; Write a program to print a pyramid pattern of stars of height n.
pyramid=int(input("Enter height(no.of rows) in pyramid:"))
for m in range(1,pyramid+1):
    for n in  range(pyramid-m):
        print(" ",end=' ')#create spaces
    for o in range(2*m-1):#create odd no. of stars
        print("*",end=" ")    
    print()    