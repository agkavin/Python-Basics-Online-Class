import random

print("🎮 Welcome to the Magic Number Jump Game!")
print("Guess a number between 1 and 10.")
print("Type 0 to skip your turn. Type -1 to exit the game.\n")

magic_number = random.randint(1, 10)
inactive = False

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("That's not a number. Try again.")
        continue

    if guess == -1:
        print("You chose to quit the game. Bye!")
        break

    if guess == 0:
        print("You skipped your turn!\n")
        inactive = True
        continue

    if guess < 1 or guess > 10:
        print("Please guess a number between 1 and 10!")
        continue

    if inactive and guess == magic_number:
        print("Oops! The magic number was inactive this round. Try again!\n")
        pass
        inactive = False
        continue

    if guess == magic_number:
        print("🎉 Correct! You found the magic number!")
        break
    else:
        print("❌ Not correct. Try again!\n")
