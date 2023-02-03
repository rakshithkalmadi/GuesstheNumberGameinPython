import random

target = random.randint(1, 10)
tries = 5

while tries > 0:
    player_guess = int(input("Enter your guess: "))
    if player_guess == target:
        print("Congratulations! You guessed the number in", 5 - tries + 1, "tries.")
        break
    elif player_guess < target:
        print("The target number is higher.")
    else:
        print("The target number is lower.")
    tries -= 1

if tries == 0:
    print("Sorry, you ran out of tries. The target number was", target)
