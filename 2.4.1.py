import random as rnd

num = rnd.randint(1, 100)
for i in range(6):
    guess = int(input("Guess a number between 1 and 100: "))
    if i != 5:
        if guess == num:
            print("You win!")
        elif guess < num:
            print("Too low!")
        elif guess > num:
            print("Too high!")
    else:
        print(f"You lose! The number was {num}.")