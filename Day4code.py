#code 16 ; program to check vowel or consonents;
char=input("Enter exactly one char:")
if len(char)==1 and char.isalpha():
    char_lower=char.lower
    if char_lower=='aeiou':
        print("charecter is vowel")
    else:
        print("charecter is consonent")
else:
    print("invalid input:enter a single alphabatic charater")   



#code 17 ; check if entered character is alphabet,digit,or special charater ;
ch=input("Enter a charater:")
if len(ch)==1:
    if ('a'<=ch<='z') or ('A'<=ch<='Z'):
        print("Charater is alphabet:")
    elif ('0'<=ch<='9'):
        print("Character is number")
    else :
        print("charecter is special symbol")
else :
    print("please enter single charater ")  



#code 18 ; Grade calculator;
marks=int(input("Enter your marks:"))
if (marks>=80) and (marks<=100):
    print("your grade is A")
elif (marks>=60) and (marks<=79):
    print("your grade is B")
elif (marks>=40) and (marks<=59): 
    print("your grade is C")  
elif (marks>=30) and (marks<=39):
    print("your grade is D") 
elif (marks>=0)and(marks<=29):
     print("you are fail")
else:
    print("Enter your marks between 0 to 100") 


   
#code 19 ; check number if it is div by both 3 and 5.
num=int(input("Enter a number to check it is div by both 3 and 5:"))
if num%3==0 and num%5==0 :
    print("Number is div by both 3 and 5")
else : 
    print("Number is not div by both 3 and 5") 

     

#code 20 ; voting age identifier;
age=int(input("Enter yoy age:"))
if age>= 18:
    print("You are eligible to vote")
elif age<=0:
    print("Enter an eligible age ")
else:
    ("You are not eligible to vote")        
            

