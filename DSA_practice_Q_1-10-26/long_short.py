sentence = input("Enter a sentence: ")

words = sentence.split()

longest = words[0]
shortest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest word:", longest)
print("Shortest word:", shortest)