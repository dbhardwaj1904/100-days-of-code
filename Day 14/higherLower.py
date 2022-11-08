from secrets import choice
from heading import heading
from versus import versus
from data import data
import random

def user_picks():
    return random.choice(data)

def print_details(user_picked):
    name = user_picked['name']
    description = user_picked['description']
    country = user_picked['country']
    return f"{name}, {description} from {country}"

def comparing_followers(user, a, b):
    if (a > b):
        return user == "a"
    else:
        return user == "b"

def higherLower():
    print(heading)
    score = 0
    continueGame = True
    choice_a = user_picks()
    choice_b = user_picks()

    while continueGame:
        choice_a = user_picks()
        choice_b = user_picks()
        while (choice_a == choice_b):
            choice_b = user_picks()
        print(f"Compare A: {print_details(choice_a)}")
        print(versus)
        print(f"Against B: {print_details(choice_b)}")
        user_choice = input(f"Who has more followers: A or B? ").lower()
        a_followers = choice_a['follower_count']
        b_followers = choice_b['follower_count']

        check = comparing_followers(user_choice, a_followers, b_followers)
        if (check):
            score += 1
        else:
            continueGame = False
            print(f"Sorry, that's wrong. Final score: {score}")

higherLower()