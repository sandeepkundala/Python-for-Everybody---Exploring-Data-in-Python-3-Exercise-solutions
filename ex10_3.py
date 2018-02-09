# Chapter 10
# Exercise 3: Write a program that reads a ﬁle and prints the letters in decreasing
# order of frequency. Your program should convert all the input to lower case and
# only count the letters a-z. Your program should not count spaces, digits, punctua-
# tion, or anything other than the letters a-z. Find text samples from several diﬀerent
# languages and see how letter frequency varies between languages. Compare your
# results with the tables at wikipedia.org/wiki/Letter_frequencies.

letter_dict = dict()
fname = input('Enter a file name:')
fopen = open(fname)
for line in fopen:
    line = line.strip()
    line = line.lower()
    for char in line:
        if char>='a' and char<='z':
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] = letter_dict[char] + 1

lst = list()
lst = list(letter_dict.items())

lst.sort()

for key, val in lst:
    print(key, val)
