# Chapter 7
# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun,
# they add a harmless Easter Egg to their program Modify the program that prompts
# the user for the ﬁle name so that it prints a funny message when the user types in
# the exact ﬁle name “na na boo boo”. The program should behave normally for all
# other ﬁles which exist and don’t exist.

fname = input('Enter the file name: ')
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
try:
    fh = open(fname)
    count = 0
    for line in fh:
        count = count + 1
    print('There were ', count, ' subject lines in ', fname)
except:
    print('File cannot be opened:', fname)
