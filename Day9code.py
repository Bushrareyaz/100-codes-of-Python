#code 41 ;Write a program to check whether a number n is a palindrome (reads the same reversed).
#using sliciing a string.
palindrome=input("Enter a number or a string:")
if palindrome==(palindrome[::-1]):
    print(palindrome,"is a palindrome")
else:
    print(palindrome," is not a palindrome:") 



#code 42;   Write a program to replace all zeros in a number n with the digit 5.
input_num=input("enter a number:")
replace_num=input_num.replace('0','5')
r=int(replace_num)
print("modified integer is",r)



#code 43 ; Write a program to find the sum of the first and last digit of a number n.
n=input("enter digits:")
first=int(n[0])
last=int(n[-1])
sum=first+last
print("sum of first and last digit is:",sum)


#NUMBER CLASSFICATION(PRIME,SPECIAL NUMBERS)
#code 44 ; Write a program to read a number and check whether it is prime or not.

num=int(input("enter a number to check it is prime or not:"))
if num <= 1:
    print(num,"is a not a prime number.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")     



#code 45; Write a program to display all prime numbers from 1 to n.
num_prime=int(input("enter number upto to you want to print prime nubmer:"))
for j in range(2,num_prime+1):
    for k in range(2,j):
        if j%k==0:
            break
    else:
        print("prime numbers are:",j)    

