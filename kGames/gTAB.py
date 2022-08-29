from time import sleep as wait

wait(1)
print('Welcome to kGames!')
wait(2)
print('Here, you can play some very cool games made with hard-work and heart!')
wait(4)
print('Okay, now, enjoy some cool and great games!')

print('"m" = Math Quiz \n"ml" = Mad Libs')

gCHOOSE = input('∂g.play ')
if gCHOOSE == "m":
    print('Loading..')
    wait(1)
    import math
elif gCHOOSE == "ml":
    print('Loading..')
    wait(1)
    import ml
