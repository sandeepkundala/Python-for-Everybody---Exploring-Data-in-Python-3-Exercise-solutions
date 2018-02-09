# Chapter 4
# Exercise 7: Rewrite the grade program from the previous chapter using a function
# called computegrade that takes a score as its parameter and returns a grade as a
# string.

def computegrade(score):
    try:
        score = float(score)
        if score <= 1.0 and score >=0.0:
            if score >= 0.9:
                print('A')
            elif score >= 0.8:
                print('B')
            elif score >= 0.7:
                print('C')
            elif score >= 0.6:
                print('D')
            elif score < 0.6:
                print('F')
        else:
            print('Bad Score')

    except:
        print('Bad Score')

score = input('Enter score: ')
computegrade(score)
