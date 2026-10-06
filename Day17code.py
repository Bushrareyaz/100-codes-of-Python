#code 81 ; Write a program to find the sum and average of all elements in an array.
arr=[5,6,3,8,9,7]
sum=0
for i in arr:
    sum+=i
x=len(arr)
average=sum/x
print("sum of elements is ",sum) 
print("average of elements is ",average)   



#code 82 ; Write a program to find the largest and smallest element in an array.
marks=[40,55,48,70,34,60]
largest=marks[0]
smallest=marks[0]
for i in marks:
    if i >largest:
        largest=i
    elif i < smallest:
        smallest=i
print( 'largest is',largest)
print( 'smallest is',smallest)



#codee 83 ; Write a program to count the number of even and odd elements in an array.
prices=[34,89,67,48,90,22]
odd=0
even=0
for i in prices:
    if i%2==0:
        odd+=1
    else:
        even+=1
print("Number od even elements :",even) 
print("Number od odd elements :",odd) 



#code 84 ; Write a program to search for an element in an array (linear search).
marks = [40, 55, 48, 70, 34, 60]
target = int(input("Enter the element to search: "))

found = False

for i in range(len(marks)):
    if marks[i] == target:
        print("Element found at index",i)
        found = True
        break

if not found:
    print("Element not found")



#code 85 ;Write a program to reverse the elements of an array.
cars=['volvo','ford','BMW',"Toyota"]
reverse=cars.reverse()
print(cars)    