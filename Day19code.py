#code 91 ; Write a program to find the sum of all even-indexed and odd-indexed elements separately.
marks=[25,71,82,94,56,91,75]
odd_index=marks[1::2]
sumodd=0
sumeven=0
even_index=marks[::2]
for i in odd_index:
    sumodd+=i
for j in even_index:
    sumeven+=j
print("sum of even_index element is:",sumeven)  
print("sum of odd_index element is:",sumodd)  


#Challenge round (mix everything)
#code 92 ; Write a program to check whether a number is prime, using a function/method.
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")




#code 93 ; Write a program to print all prime numbers between two given numbers a and b.
def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n** 0.5)  + 1, 2):
        if n % i == 0:
            return False
    return True

a = int(input("Enter first number: "))
b = int(input("Enter last number:"))
print(f"Prime numbers between {a} and {b}:")
count = 0
for num in range(a, b + 1):
    if prime(num):
        print(num, end=" ")
        count += 1

print(f"\nTotal prime numbers: {count}")



#code 94 ; Write a program to find the sum of digits of a number repeatedly until a single digit remains.
def sum_of_digits(n):
    """Return the sum of all digits of n."""
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


num = int(input("Enter a number: "))

while num >= 10:
    num = sum_of_digits(num)

print("Single digit result:", num)



#code 95 ; Write a program to count the number of prime digits present in a number n.
def count_prime_digits(n):
    """Return how many digits of n are prime (2, 3, 5 or 7)."""
    n = abs(n)
    count = 0
    while n > 0:
        digit = n % 10
        if digit in (2, 3, 5, 7):
            count += 1
        n //= 10
    return count


num = int(input("Enter a number: "))
print("Number of prime digits:", count_prime_digits(num))

