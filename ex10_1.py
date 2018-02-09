# Exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages from
# each person using a dictionary.
# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the list in
# reverse order and print out the person who has the most commits.
#
# Sample Line:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

email_dict = dict()
fname = input('Enter a file name:')
fopen = open(fname)
for line in fopen:
    line = line.strip()
    if line.startswith('From '):
        s = line.split()
        email = s[1]
        if email not in email_dict:
            email_dict[email] = 1
        else:
            email_dict[email] = email_dict[email] + 1
lst = list()
for key, val in list(email_dict.items()):
    lst.append((val,key))

lst.sort(reverse=True)
val, key = lst[0]
print(key, val)
