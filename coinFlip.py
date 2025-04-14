import random

def coin_flip():
    user_guess = input("Heads or Tails?").lower()
    flip = random.choice(["heads", "tails"])

    print("The coin landed on", flip)
    if user_guess == flip:
        print("You win!")
    else:
        print("You lose!")
coin_flip()

    