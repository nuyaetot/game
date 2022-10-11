import random as ran

print("Привет, сейчас ты будешь играть в самую увлекательную игру в мире)")
am = ran.randint(4, 30)
komp = 0
while am > 1:
    user = int(input("твой ход(ты можешь убрать 1,2 или 3 камня из кучи)"))
    am = am - user
    if am == 1:
        print("поздравляю, ты выиграл")
        break
    else:
        print(am, "камни в куче после твоего хода")
    if am > 3:
        komp = ran.randint(1, 3)
    if am == 3:
        komp = ran.randint(1, 2)
    if am == 2:
        komp = ran.randint(1, 1)
    am = am - komp
    if am == 1:
        print("к сожалению, ты проиграл :(")
    else:
        print(am, "камни в куче после хода компа")
