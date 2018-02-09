# Chapter 8
# Exercise 4: Write a program to open the ﬁle romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split function.
# For each word, check to see if the word is already in a list. If the word is not in
# the list, add it to the list.
fh = input('Enter file: ')
fopen = open(fh)
word = []
for line in fopen:
    words = line.split()
    for s in words:
        word.append(s)
word.sort()
print(word)
