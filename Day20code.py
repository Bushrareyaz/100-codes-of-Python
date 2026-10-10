#code 96 : Write a program to check whether a number is a palindrome and a prime at the same time.
num=int(input("Enter number"))
original=num
reverse=0
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
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(original, "is a palindrome")
else:
    print(original, "is not a palindrome")  


