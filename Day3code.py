#Today we are doing if else statement in python..lets goooo!!!!!! 

#code 11 ; progrem to read a no. and check whether it is odd or even.
num_check=int(input("Enter number to check:"))
if num_check%2==0:
    print("Entered Number is even:")
else:
    print("Entered Number is odd:") 



#code 12 ; program to check no. is positive,negative or zer0.
num=int(input("Enter any number:"))
if num>0:
    print("Number is positive:")
elif num<0:
    print("Number is negative:")
else:
    ("print number is zero:")



#code 13 ;find largest among them.
num_1=int(input("Enter first number:"))
num_2=int(input("Enter second number:"))   
num_3=int(input("Enter third number:")) 
if num_1 > num_2 and num_1 > num_3:
    print("Number first is largerst that is:",num_1) 
elif num_2 > num_3 and num_2 > num_1:
    print("Number second is largest that is:",num_2)
else:
    print("Number third is largest that is:",num_3) 

   

#code 14 ;find the smallest number
num_4=int(input("Enter first number:"))
num_5=int(input("Enter second number:"))   
num_6=int(input("Enter third number:")) 
if num_4 < num_5 and num_4 < num_6:
    print("Number first is smallest that is:",num_4) 
elif num_5 < num_4 and num_5 < num_6:
    print("Number second is smallest that is:",num_5)
else:
    print("Number third is smallest that is:",num_6)    



#code 15 ; program to find the years are leap year or not;
year=int(input("Enter year to find it was leap year or not:"))
if year%4==0 and year%100==0 or year%4==0:
    print("The year is leap year:")
else:
    print("The yaer is not a leap year:")   
    
