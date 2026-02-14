import random

target_number = random.randrange(1, 1001)
counter = 0
guess = 0

while guess != target_number:
    guess = int(input("Pick a number between 1 and 1000: "))
    if guess > 1000 or guess < 1:
        print("Enter a number between 1-1000")
    else:
        counter += 1
        if guess < target_number:
            print("Higher")
        elif guess > target_number:
            print("Lower")
        elif guess == target_number:
            print(f"It took you {counter} guesses to get the target number which was {target_number}!")