# CHAPTER 3
# Exercise 2: Rewrite your pay program using try and except so that your pro-
# gram handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input

hr = input('Enter Hours:')
r = input('Enter Rate:')
try:
    hr = float(hr)
    r = float(r)
    if hr>40:
        normal_hr = 40
        extra_hr = hr-40
    else:
        normal_hr = hr
        extra_hr = 0
    pay = normal_hr*r + extra_hr*1.5*r
    print('Pay:', pay)
except :
    print('Error, please enter numeric input')
