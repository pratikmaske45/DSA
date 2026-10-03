n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even elements:", even)
print("Number of odd elements:", odd)