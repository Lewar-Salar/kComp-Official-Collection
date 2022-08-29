from time import sleep as wait

def script():
    wait(1)

    print('Game is loading! Please wait..')
    wait(5)
    print('Scripts loaded!')
    wait(1)

    points = 0

    q1 = input('21 + 248 = ')
    q2 = input('45 - 24 = ')
    q3 = input('7 x 12 = ')
    q4 = input('59 + 23 = ')
    q5 = input('8 ÷ 2 = ')
    q6 = input('58 - 34 = ')
    q7 = input('2 ÷ 2 = ')
    q8 = input('43 x 10 = ')
    q9 = input('443 - 128 = ')
    q10 = input('64 + 44 = ')

    if q1 == "269":
        print('Question 1: Correct!')
        points += 1
    else:
        print('Question 1: Wrong!')
    if q2 == "21":
        print('Question 2: Correct!')
        points += 1
    else:
        print('Question 2: Wrong!')
    if q3 == "84":
        print('Question 3: Correct!')
        points += 1
    else:
        print('Question 3: Wrong!')
    if q4 == "88":
        print('Question 4: Correct!')
        points += 1
    else:
        print('Question 4: Wrong!')
    if q5 == "4":
        print('Question 5: Correct!')
        points += 1
    else:
        print('Question 5: Wrong!')
    if q6 == "24":
        print('Question 6: Correct!')
        points += 1
    else:
        print('Question 6: Wrong!')
    if q7 == "1":
        print('Question 7: Correct!')
        points += 1
    else:
        print('Question 7: Wrong!')
    if q8 == "430":
        print('Question 8: Correct!')
        points += 1
    else:
        print('Question 8: Wrong!')
    if q9 == "315":
        print('Question 9: Correct!')
        points += 1
    else:
        print('Question 9: Wrong!')
    if q10 == "108":
        print('Question 10: Correct!')
        points += 1
    else:
        print('Question 10: Wrong!')

    wait(1)
    print('You got {}/10 questions correct!'.format(points))
    y_or_n = input('Would you like to play again? ')
    if y_or_n == "y":
        script()
    elif y_or_n == "n":
        import gTAB

# script.Start()

script()
