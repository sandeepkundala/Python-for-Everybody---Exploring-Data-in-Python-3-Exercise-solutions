# Chapter 4
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate).

def computepay(hr, r):
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

hr = input('Enter Hours:')
r = input('Enter Rate:')
computepay(hr,r)
