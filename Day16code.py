#code 76 ; Write a program to check whether two strings are anagrams of each other.
#An anagram is a word or phrase made by rearranging the exact same letters from another word or phrase.

s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")