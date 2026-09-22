#code 36; Write a program to find the product of all digits of a number n.
n=int(input("Enter number to find product of all digits:"))
prod=1
while n > 0:
    digit = n % 10 
    prod = prod * digit
    n = n // 10
print("product are:",prod)       
    
