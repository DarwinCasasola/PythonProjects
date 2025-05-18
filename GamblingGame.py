import random

money = 100 
print("Welcome to the Coin Flip Game!")
print("You start with $100.")

while money > 0:
    print(f"\nYou have ${money}.")
    bet = int(input("How much do you want to bet? "))

    if bet > money:
        print("You can't bet more than you have.")
        continue

    choice = input("Heads or Tails? (h/t): ").lower()
    if choice not in ['h', 't']:
        print("Invalid Choice.")
        continue
    flip = random.choice(['h', 't'])
    print(f"The coin flip result is: {'Heads' if flip == 'h' else 'Tails'}")

    if choice == flip:
        print(f"You win!")
        money += bet
    else:
        print(f"You lose!")
        money -= bet
    again = input("Play again? (y/n): ").lower()
    if again != 'y':
        break

print(f"\n Game Over! You leave with ${money}.")
