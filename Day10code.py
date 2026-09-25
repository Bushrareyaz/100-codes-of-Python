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

        
