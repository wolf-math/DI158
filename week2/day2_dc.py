# Instructions
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

word = input("Enter a word: ")
word_dict = {}

for i in range(len(word)):
    if word[i] in word_dict:
        word_dict[word[i]].append(i)
    else:
        word_dict[word[i]] = [i]

print(word_dict)