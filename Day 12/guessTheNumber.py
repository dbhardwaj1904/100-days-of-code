from random import randint

try_again = True
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
NO_LEVEL_TURNS = 1

def checkNumber(user, computer):
    if (user > computer):
        print("Too high.")
        return False
    elif (user < computer):
        print("Too low.")
        return False
    else:
        print("You win. Thanks for playing...")
    return True

def chooseDifficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ->  ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS
    else:
        return 1

def guessTheNumber():
    global try_again
    while try_again == True:
        print("Welcome to the Number Guessing Game!")
        print("Computer thinking of number")
        computer = randint(1, 100)
        attempts = chooseDifficulty()
        while attempts != 0:
            print(f"You have {attempts} remaining to guess the number...")
            user = int(input("Make a guess ->  "))
            if checkNumber(user, computer):
                userTry = input("\nWanna play again (Type yes or no) ? ")
                if userTry == "yes":
                    try_again = True
                else:
                    try_again = False
                break
            if attempts != 0:
                print("Guess again.\n")
            attempts = attempts - 1
        if attempts == 0:
            userTry = input("\nGAME OVER. You can win next time maybe. Wanna try (Type yes or no) ? ")
            if userTry == "yes":
                try_again = True
            else:
                try_again = False

guessTheNumber()