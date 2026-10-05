#code 76 ; Write a program to check whether two strings are anagrams of each other.
#An anagram is a word or phrase made by rearranging the exact same letters from another word or phrase.

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")



#code 77 ; Write a program to find the first non-repeating character in a string.
s = input("Enter a string: ")

counts = {}

# Pass 1: count how many times each character appears
for ch in s:
    counts[ch] = counts.get(ch, 0) + 1

# Pass 2: find the first character that appears only once
result = None
for ch in s:
    if counts[ch] == 1:
        result = ch
        break  # stop at the first match

if result is not None:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")



#code 78 ; Write a program to replace all occurrences of a character with another character in a string.
text = input("Enter a string: ")
old_ch = input("Enter the character to replace: ")
new_ch = input("Enter the new character: ")
result = ""
for ch in text:
    if ch == old_ch:
        result += new_ch
    else:
        result += ch
print("Modified string:", result)
print(text.replace(old_ch, new_ch))  



#code 79 ; Write a program to toggle the case of each character in a string.
str = input("Enter a string: ")
result = ""
for ch in str:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
print("Toggled string:", result)
print(str.swapcase())


# ARRAYS / LISTS ;

# code 80; Write a program to read n elements into an array and print them.
arr1=[1,5,6,45,67]
print(arr1[4])


