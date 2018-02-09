# Chapter 7
# Exercise 2: Write a program to prompt for a ﬁle name, and then read through the
# ﬁle and look for lines of the form:
# X-DSPAM-Confidence:0.8475
# When you encounter a line that starts with “X-DSPAM-Conﬁdence:” pull apart
# the line to extract the ﬂoating-point number on the line. Count these lines and
# then compute the total of the spam conﬁdence values from these lines. When you
# reach the end of the ﬁle, print out the average spam conﬁdence.

# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745

# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
count = 0
total = 0
fh = open('C:/Users/sandeep.kundala/Documents/python/mbox-short.txt')
for line in fh:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count+1
        atpos = line.find(':')
        total = total + float(line[atpos+1:])
    else:
        continue
avg = total/count
print('Average spam confidence:', avg)
