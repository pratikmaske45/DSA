n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

print("Original array:", arr)

print("Array in reverse order:")

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")