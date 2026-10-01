# Write a program to accept N integers into an array and calculate and display the sum of all the elements. 
n = int(input("Enter N: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

sum = 0

for num in arr:
    sum = sum + num

print("Sum =", sum)

