#code 46 ; Write a program to display the first n prime numbers.
n = int(input("Enter how many prime numbers: "))
count = 0
num = 2

while count < n:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count += 1
    num += 1


        
#code 47 ; Write a program to check whether a number is an Armstrong number.
dig=int(input("Enter number to check it is Armstrong:"))
original=dig
sum=0
while dig > 0 :
    al=dig%10 #last digit number
    sum=sum+al*al*al #cube it and add to add
    dig=dig//10# remove last digit
if sum==original:
    print(original,"is an Armstromg")
else:
    print(original,"is not an Armstrong")    


    
#code 48 ; Write a program to display all Armstrong numbers from 1 to n.
value=int(input("Enter number till you want to display Armstrong:"))
for j in range(1,value+1):
    original = j
    temp = j
    sum_1 = 0
    while temp>0:
        digit=temp%10
        sum_1=sum_1+digit*digit*digit
        temp=temp//10
    if sum_1==original:
        print(original)    



# code 49 ; Write a program to check whether a number is a perfect number.
per_num=int(input('Enter number to check if it is a perfect number:'))
sum=0
for k in range(1,per_num):
    if per_num%k==0:
        sum+=k
if sum==per_num:
    print(per_num,"is a perfect number")
else:
    print(per_num,"is not a perfect number")    




#code 50; Write a program to check whether a number is a strong number (sum of factorials of its digits) is same as digit itself.
str_num=int(input("Enter a number to check if it is strong number: "))
sum_2=0
real=str_num
while str_num>0:
        m=str_num%10
        fact=1
        for l in range(1,m+1): 
            fact=fact*l
        sum_2=sum_2+fact
        str_num=str_num//10
if sum_2==real:
    print(real,"is a strong number")         
else:
    print(real,"is not a strong number")






    