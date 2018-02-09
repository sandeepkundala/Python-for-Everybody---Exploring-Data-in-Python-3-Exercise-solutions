# Chapter 10
# Exercise 2: This program counts the distribution of the hour of the day for each
# of the messages. You can pull the hour from the “From” line by ﬁnding the time
# string and then splitting that string into parts using the colon character. Once
# you have accumulated the counts for each hour, print out the counts, one per line,
# sorted by hour as shown below.

hour_dict = dict()
fname = input('Enter a file name:')
fopen = open(fname)
for line in fopen:
    line = line.strip()
    if line.startswith('From '):
        s = line.split()
        time = s[5]
        hours = time.split(':')
        if hours[0] not in hour_dict:
            hour_dict[hours[0]] = 1
        else:
            hour_dict[hours[0]] = hour_dict[hours[0]] + 1

lst = list()
lst = list(hour_dict.items())

lst.sort()

for key, val in lst:
    print(key, val)
