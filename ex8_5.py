# Chapter 8
# Exercise 5: Write a program to read through the mail box data and when you
# ﬁnd line that starts with “From”, you will split the line into words using the split
# function. We are interested in who sent the message, which is the second word on
# the From line.
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# You will parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a
# count at the end.
fh = input('Enter file: ')
fopen = open(fh)
count = 0
for line in fopen:
    line = line.strip()
    if line.startswith('From:'):
        count = count + 1
        s = line.split()
        print(s[1])
print('There were ',count,' lines in the file with From as the first word')
