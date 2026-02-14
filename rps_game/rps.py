import random

user_score = 0
program_score = 0

while program_score < 2 and user_score < 2:
    user_answer = input("Pick Rock, Paper, or Scissors: ").lower()
    if user_answer not in ("rock", "paper", "scissors"):
        print("Enter a valid answer")
    else:
        program_answer = random.randrange(1, 4)
        if program_answer == 1:
            print("Rock")
            program_answer = "rock"
        elif program_answer == 2:
            print("Paper")
            program_answer = "paper"
        else:
            print("Scissors")
            program_answer = "scissors"
        
        if user_answer == program_answer:
            print("It's a draw!")
            print(f"Score: You {user_score} - Computer {program_score}")
        elif user_answer == "rock" and program_answer == "scissors":
            print("You won this round!")
            user_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")
        elif user_answer == "paper" and program_answer == "rock":
            print("You won this round!")
            user_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")
        elif user_answer == "scissors" and program_answer == "paper":
            print("You won this round!")
            user_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")
        elif program_answer == "rock" and user_answer == "scissors":
            print("I won this round!")
            program_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")
        elif program_answer == "paper" and user_answer == "rock":
            print("I won this round!")
            program_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")
        elif program_answer == "scissors" and user_answer == "paper":
            print("I won this round!")
            program_score += 1
            print(f"Score: You {user_score} - Computer {program_score}")

        if user_score == 2:
            print("Congratulations, you won!")
        
        if program_score == 2:
            print("I won, better luck next time!")


     
