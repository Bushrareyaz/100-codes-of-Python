#code 71 ; Write a program to reverse a string.

sentence=input("Enter a string:")
reverse=(sentence[::-1])
print("Reverse of string is ",reverse)



#code 72 ; Write a program to check whether a string is a palindrome.
#palindrome;sentence reads same backwards

s=input("Enter a string:")
r=(s[::-1])
if r==s:
    print(s,"is palindrome.")
else:
    print(s,"is not a palindrome.")



#code 73 ;Write a program to convert a string to uppercase and lowercase without inbuilt case functions.
poem="To be tough is to be fragile; to be tender is to be truly fierce."
upper= " "
lower= " "
for ch in poem:
    if  'a'<=ch<='z' :
        upper = upper + chr(ord(ch) - 32)
    else:
        upper = upper + ch
    if 'A' <= ch <= 'Z':
        lower = lower + chr(ord(ch) + 32)
    else:
        lower = lower + ch

print("Uppercase:", upper)
print("Lowercase:", lower)



#code 74 ; Write a program to count the frequency of each character in a string.

from collections import Counter
text = "To be tough is to be fragile; to be tender is to be truly fierce."
# The Counter object acts like a dictionary automatically
frequency = Counter(text)
print("Character Frequencies:", dict(frequency))



#code 75 ; Write a program to remove all spaces from a string.
words="And still, like air, I'll rise Still I Rise"
no_space=words.replace(" ","")
print(no_space)