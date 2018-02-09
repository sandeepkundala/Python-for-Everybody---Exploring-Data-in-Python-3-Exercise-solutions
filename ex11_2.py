# Chapter 11
# Exercise 2: Write a program to look for lines of the form
# `New Revision: 39772`
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
# Enter file:mbox.txt
# 38549.7949721
# Enter file:mbox-short.txt
# 39756.9259259

import re
count = 0
total = 0
fname = input('Enter file name: ')
fh = open(fname)

for line in fh:
    line = line.rstrip()
    x = re.findall('^New Revision:',line)
    if len(x)>0:
        count = count+1
        x = line.split()
        total = total + float(x[2])
avg = total/count
print(avg)
