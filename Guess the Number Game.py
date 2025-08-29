number=9

while True:
    Gnumber=int(input("guess a number. between 1 to 10"))
    if Gnumber<number:
        print("you take a small number, try again")
    elif Gnumber>number:
        print("your number is too high")
    elif Gnumber==number:
        print("congratulation ,you got this")
        break
