n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

search = int(input("Enter the number to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Number is present at position:", i + 1)
        found = True
        break

if found == False:
    print("Number is not present in the array")