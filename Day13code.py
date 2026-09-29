#code 61 ;Write a program to find the sum of the series 1 + 1/2 + 1/3 + ... + 1/n.
n=int(input("Enter value of n of series 1/n till there:"))
sum=0
for k in range(1,n+1):
    sum+=1/k    
print(f"the sum of series of 1/n till{n} is: {sum}")  


