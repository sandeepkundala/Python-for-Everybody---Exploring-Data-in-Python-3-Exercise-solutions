# Chapter 9
# Exercise 3: Write a program to read through a mail log, build a histogram using
# a dictionary to count how many messages have come from each email address, and
# print the dictionary.
# Exercise 4: Add code to the above program to ﬁgure out who has the most
# messages in the ﬁle.
# After all the data has been read and the dictionary has been created, look through
# the dictionary using a maximum loop (see Section [maximumloop]) to ﬁnd who
# has the most messages and print how many messages the person has.
email_dict =dict()
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
print(email_dict)
flag =0
for key in email_dict:
    if flag==0:
        maximum = email_dict[key]
        max_key = key
        flag = 1
    else:
        if maximum < email_dict[key]:
            maximum = email_dict[key]
            max_key = key
        else:
            continue
print(max_key, maximum)
