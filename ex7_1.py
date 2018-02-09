# Chapter 7
# Exercise 1: Write a program to read through a ﬁle and print the contents of the
# ﬁle (line by line) all in upper case.

fh = open('C:/Users/sandeep.kundala/Documents/python/mbox.txt')
for line in fh:
    print(line.upper())
