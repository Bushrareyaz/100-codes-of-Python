#code 51 ; Write a program to check whether a number is an automorphic number.
#An automorphic number is a number whose square ends with the digits of the number itself eg,(5)^2=25,(6)^2=36 in last number is 5 and 6

n=int(input("Enter number to check:"))
original=n
sq=n*n
l=sq%10
if l==original:
     print(original,"is an automorphic number")
else:
    print(original,"is not an automorphic number")
    



#code 52 ; Write a program to check whether a number is a Harshad (Niven) number
#A Harshad number (also called a Niven number) is an integer that is completely divisible by the sum of its own digits.
num=int(input("Enter number to check if it is Harshad(Niven) number:"))
real=num
sum=0
while num>0:
    m=num%10
    sum+=m
    num=num//10
if real%sum==0:
    print(real,"is a Harshad (Niven) number")
else:
    print(real,"Not a Harshad (Niven) number")    



#code 53 ; Write a program to find all factors (divisors) of a number n.
num_2=int(input("Enter number to find factors :"))
for i in range(1,num_2+1):
        if num_2%i==0:
          print(i,"\n")



#code 54; Write a program to count the number of factors of a number n.
num_3=int(input("Enter number to find no. of factors :"))
count=0
for j in range(1,num_3+1):
        if num_3%j==0:
                count+=1
print(count)
       


#code 55 ; Write a program to find the GCD (HCF) of two numbers.
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

hcf = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

print("HCF of", a, "and", b, "is", hcf)