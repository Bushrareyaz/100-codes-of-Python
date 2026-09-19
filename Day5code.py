#code 21 ; display all natural no. till input n 
n=int(input("Enter number till you want to display natural number:"))
for i in range(1,n+1):
    print(i)



#code 22 ; display code 21 in reverse;
num=int(input("Enter number to reverse all natural number:"))
for j in range(num,0,-1): #n=start,0=stop,-1=step
    print(j)



#code 23 ; display all odd number from 1 to input by user
num_1=int(input("Enter number to display all odds:"))
for odd in range(1,num_1+1):
    if odd%2 !=0:
        print(odd)
        


#code 24 ; display all even from 1 to input by user
num_2=int(input("Enter number to display all even:"))
for even in range(1,num_2+1):
    if even%2 ==0:
        print(even)



#code 25 ; sum of all natural number from 1 to input by user
num_3=int(input("Enter natural number to display their sum "))
sum=0
for z in range(1,num_3+1):
    sum+=z
print("sum of natural numbers till",num_3,'is:',sum)