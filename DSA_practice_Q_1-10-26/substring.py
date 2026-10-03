string = input("Enter a string: ")
substring = input("Enter substring to search: ")

count = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        print("Substring found at position:", i + 1)
        count = count + 1

print("Total occurrences:", count)