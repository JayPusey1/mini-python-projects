import random

n = int(input("Enter a Number: "))
streak = 0
previous_flip = 0
loops = 0

while streak < n:
    flip = random.randrange(1, 3)
    current_flip = flip
    if flip == 1:
        print("Heads ")
    elif flip == 2:
        print("Tails ")
    if current_flip == previous_flip:
        streak += 1
    else:
        streak = 1
    previous_flip = flip
    loops += 1
if previous_flip == 1:
    last_flip = "Heads"
else:
    last_flip = "Tails"
print(f"It took {loops} flips to reach {n} {last_flip} in a row")
