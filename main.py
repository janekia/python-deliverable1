
score = 0
holes = 0
par = 0
name = ""

name = input("What is your name? ")


holes = int(input(f"Hi {name}! Would you like to play 3 or 6 holes today? "))


par = 0


if holes == 3:
    par = 3

    putt1 = int(input("How many putts for hole 1? "))
    score += putt1


    putt2 = int(input("How many putts for hole 2? "))
    score += putt2


    putt3 = int(input("How many putts for hole 3? "))
    score += putt3

parsum = par
x = score - parsum

if score > parsum:
        print(f"Nice try, {name}! Your total score  was  + {score - parsum} over par.")
elif score < parsum:
        print(f"Great job, {name}! Your total score  was - {score - parsum} under par.")
else:
        print(f"Good game, {name}! Your total score was right on par.")



if holes == 6:
    par = 3

    putt1 = int(input("How many putts for hole 1? "))
    score += putt1

    putt2 = int(input("How many putts for hole 2? "))
    score += putt2

    putt3 = int(input("How many putts for hole 3? "))
    score += putt3


    putt4 = int(input("How many putts for hole 4? "))
    score += putt4


    putt5 = int(input("How many putts for hole 5? "))
    score += putt5


    putt6 = int(input("How many putts for hole 6? "))
    score += putt6

    parsum = par
    x = score - parsum


    if score > parsum:
        print(f"Nice try, {name}! Your total score was + {score - parsum} over par.")
    elif score < par_sum:
        print(f"Great job, {name}! Your total score was - {parsum - score} under par.")
    else:
        print(f"Good game, {name}! Your total score was right on par.")


