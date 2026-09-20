#code 26; Write a program to find the sum of all even numbers from 1 to n
num_1=int(input("Enter number to know even sums: "))
sum=0
for i in range(1,num_1+1):
    if i%2==0:
        sum+=i
        print(i)#gives all even numbers
print("sum of all numbers are:",sum)    #gives the sum of all even numbers



#code 27; Write a program to find the sum of all odd numbers from 1 to n.
num_2=int(input("Enter number to know odd sums:"))
sum_2=0
for j in range(1,num_2+1):
    if j%2!=0:
        sum_2+=j
        print(j) #gives all odd numbers
print("sum of all numbers are:",sum_2) #gives sum of all odd numbers



#code 28; Write a program to find the product of all natural numbers from 1 to n (factorial of n).
fac=int(input("Enter number to calculate factorial:"))
factorial=1
for num in range(1,fac+1):
    factorial=factorial*num
print("factorial of",fac,"is:",factorial)    



#code 29 ; multiplication table 
table=int(input("Enter the number you want to print table:"))
for k in range(1,11):
    print(table,'x',k,'=',table*k)



#code 30; Write a program to display all multiples of a number m up to n terms.
m=int(input("Enter number to display it's multiple:"))
n=int(input("Enter number till you want to display multiple:"))
for l in range(1,n+1):
        print(m*l)

