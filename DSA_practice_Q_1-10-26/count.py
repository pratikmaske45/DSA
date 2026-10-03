string = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

    elif ch.isdigit():
        digits = digits + 1

    else:
        special = special + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)