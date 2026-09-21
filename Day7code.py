#code 31; Write a program to count how many numbers from 1 to n are divisible by 3.
div=int(input("Enter number till you want to count divisibility:"))
count=0
for num in range(1,div+1):
    if num%3==0:
        count+=1
print("numbers that are div by 3 from 1 to",div,'are:',count)



#code 32; Write a program to display all numbers from 1 to n that are divisible by 3 or 5.
div_num=int(input("Enter number till you want to check divisibility: "))
for i in range(1,div_num+1):
    if i%3==0 and i%5==0 :
       print(i)


# NOW WORKING WITH A DIGITS OF A NUMBER
#code 33;Write a program to count the number of digits in a number n.

dig=input("Enter digits:")
length=len(dig)
print(length)



#code 34; Write a program to display all the digits of a number n (one per line).
dig_1=input("Enter number to display digits in one line:")
for j in dig_1:
    print(j)



#code 35; Write a program to find the sum of all digits of a number n.
num_2=input("Enter number to add their sum of digits:")
sum=0
for k in num_2:
    sum+=int(k)
print("Sum of all digits are:",sum)   
 






