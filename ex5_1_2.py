# Chapter 5
# Exercise 1 & 2: Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, average of the
# numbers, maximum and minimum of the numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

total = 0
count = 0
while True:
    line = input('Enter a number:')
    try:
        if line =='done':
            break
        line = float(line)
        total = total + line
        count = count + 1
        if count == 1:
            min = line
            max = line
        else:
            if min > line:
                min = line
            elif max < line:
                max = line
    except:
        print('Invalid input')
avg = total/count
print(total, count, avg, min, max)
