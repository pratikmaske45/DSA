# Write a program to accept N integers into an array and find and display the largest element, 
# second largest element, smallest element, second smallest element present in the array. 

arr = list(map(int,input("Enter number:").split()))
min=arr[0]
max =arr[0]

smin=arr[0]
smax=arr[0]

for num in arr:
    if num<min:
        smin=min
        min=num
        
    if num>max:
        smax=max
        max =num
        
print("min",min)
print("max",max)
print("second min",smin)
print("second max", smax)





