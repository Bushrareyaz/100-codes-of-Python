# code 66 ; Write a program to print a number triangle (row i contains numbers 1 to i).
n=6
for i in range(1,7):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



#code 67 ; Write a program to print Pascal's triangle for n rows.
rows = int(input("Enter no. of rows: "))
for i in range(rows):
    print(" " * (rows - i - 1), end="")   # leading spaces
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)    # next value in this row
    print()                               # move to the next line



# LEVEL 7 — STRINGS

#code 68; Write a program to find the length of a string without using an inbuilt function.
string="MY MAJOR IS COMPUTER SCIENCE"
count=0
for length in string:
    count+=1
print("Length of string is ",count)   



#code 69 ; Write a program to count the number of vowels and consonants in a string.
poem="Hope is the thing with feathers / That perches in the soul"
vowels=0
consonents=0
for ch in poem:
    if ch.isalpha():
        if ch in "AEIOUaeiou":
            vowels+=1
        else:
            consonents+=1 
print("vowels are ",vowels)                
print("consonents are ",consonents)        



#code 70 ; Write a program to count the number of words in a sentence.
sentence="Life is like riding a bicycle. To keep your balance, you must keep moving."
words=len(sentence.split())
print("No of words in string is :",words)