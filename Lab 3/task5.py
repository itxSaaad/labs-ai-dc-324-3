word = input("Enter a word: ")
reverse = ''

for i in range(len(word) - 1, -1, -1):
    reverse += word[i]
print("Reverse of the word is: ", reverse)
