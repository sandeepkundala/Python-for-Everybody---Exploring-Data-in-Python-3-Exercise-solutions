# Chapter 8
# Exercise 6: Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the user
# enters “done”. Write the program to store the numbers the user enters in a list
# and use the max() and min() functions to compute the maximum and minimum
# numbers after the loop completes.
flag = 0
num_list =[]
while True:
    num = input('Enter the number: ')
    if num == 'done':
        break
    else:
        num = int(num)
        num_list.append(num)
max = max(num_list)
min = min(num_list)
print('Maximum: ', max)
print('Minimum: ', min)
