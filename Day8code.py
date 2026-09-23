#code 36; Write a program to find the product of all digits of a number n.
n=int(input("Enter number to find product of all digits:"))
prod=1
while n > 0:
    digit = n % 10 
    prod = prod * digit
    n = n // 10
print("product are:",prod)       
    


#code; 37 Write a program to reverse a number n.
number='23456'
reverse=(number[::-1])
print("Reverse of the number n is:",reverse)

#or
num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10 
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse is:", reverse)



#code 38; Write a program to find the largest digit in a number n.
num_2=int(input("Enter digits:"))
largest=0
while num_2>0:
    digit=num_2%10 #takes last digit
    if digit>largest:
        largest=digit
    num_2=num_2//10 #remove last digit
print("Largest digit is:",largest)        



#code 39 ; Write a program to find the smallest digit in a number n.
num_3=int(input("Enter digits:"))
smallest=0
while num_3<0:
    digit=num_3%10
    if digit<smallest:
        smallest=digit
    num_3=num_3//10
print("smallest digit is:",smallest)  



# code 40 ; Write a program to count the number of even digits and odd digits in a number n.
dig=int(input("Enter digits:"))
odd = 0
even = 0
while dig > 0:
    digit = dig % 10

    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    dig = dig // 10
print("number of even digits:",even)         
print("number of odd digits:",odd)           