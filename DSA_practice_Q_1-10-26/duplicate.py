n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print("Original array:", arr)
print("Array after removing duplicates:", unique)