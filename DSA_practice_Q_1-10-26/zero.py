n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

result = []

# Add all non-zero elements
for num in arr:
    if num != 0:
        result.append(num)

# Add zeros at the end
for num in arr:
    if num == 0:
        result.append(num)

print("Original array:", arr)
print("Array after moving zeros:", result)