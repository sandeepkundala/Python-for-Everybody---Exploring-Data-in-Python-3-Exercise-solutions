# CHAPTER 3
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.

hr = input('Enter Hours:')
hr = float(hr)
r = input('Enter Rate:')
r = float(r)
if hr>40:
    normal_hr = 40
    extra_hr = hr-40
else:
    normal_hr = hr
    extra_hr = 0
pay = normal_hr*r + extra_hr*1.5*r
print('Pay:', pay)
