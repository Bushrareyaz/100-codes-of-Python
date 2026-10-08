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
#code 92 ; Write a program to check whether a number is prime, using a function/method

