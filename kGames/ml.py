from time import sleep as wait


def game():
    wait(1)
    print('Game is loading..')
    wait(4)
    print('Game loaded!')
    wait(2)
    fst = input('Enter a verb: ')
    snd = input('Enter a adjective: ')
    trd = input('Enter a verb: ')
    foth = input('Enter a meal of the day: ')
    fth = input('Enter a family member: ')
    sth = input('Enter a verb: ')
    seth = input('Enter a adjective: ')
    eth = input('Enter a verb: ')
    nth = input('Enter a song artist: ')
    tth = input('Enter a number: ')
    elth = input('Enter a number: ')
    answer = tth + elth
    twth = input('Enter a time of the day: ')
    wait(3)
    print('I ' + fst + 'up very ' + snd + ', I ' + trd + 'down to the kitchen to have ' + foth + ', but my ' + fth + ' wasn`t there.. maybe they were at work? Maybe they were ' + sth + '-ing? I didn`t know what to do. So I made my own breakfast! A ' + seth + ' cereal! And oh boy.. I ate the crap out of that cereal. Then I went to my bedroom and ' + eth + '-ed to some ' + nth + '. Then I went to do my math homework, ' + tth + ' + ' + elth + '? Hmm, oh! ' + answer + '! Let`s gooo!!!! And that is what I did this ' + twth + '.')
    wait(7)
    y_or_n = input('Would you like to play again? ')

    if y_or_n == 'y':
        game()
    elif y_or_n == 'n':
        import gTAB

wait(1)
print('Welcome to the mad-libs!')
wait(3)
print('Type "ml.start" to start.')
play = input('')
if play == 'ml.start':
    print('Loading..')
    wait(2)
    game()
else:
    print('ERROR: Invalid Command!')



