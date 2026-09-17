#code 16 ; program to check vowel or consonents;
char=input("Enter exactly one char:")
if len(char)==1 and char.isalpha():
    char_lower=char.lower
    if char_lower=='aeiou':
        print("charecter is vowel")
    else:
        print("charecter is consonent")
else:
    print("invalid input:enter a single charater")   
            

