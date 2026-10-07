#code 86 ; Write a program to find the second largest element in an array.
marks=[77,89,72,58,90,82]

arr = list(set(marks))   # remove duplicates
arr.sort()             # smallest to largest

print("Second largest =",arr[-2])



#code 87 ; Write a program to count the frequency of each element in an array.
arr=[2,5,8,9,3,4,8,7,9,0,3,1,8,1]
freq = {}

for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

for key in freq:
    print(key, "appears", freq[key], "times")



#code 88 ;  Write a program to remove duplicate elements from an array.  
brr = [1, 2, 2, 3, 4, 4, 5, 1]

result = []

for x in arr:
    if x not in result:
        result.append(x)

print("Original array:", arr)
print("After removing duplicates:", result)



#code 89 ; Write a program to sort an array in ascending order (bubble sort).
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]   # swap

print("Sorted array:", arr)



#code 90 ; Write a program to merge two arrays into one.
a = [1, 3, 5]
b = [2, 4, 6, 8]

merged = a + b

print("First array:", a)
print("Second array:", b)
print("Merged array:", merged)
