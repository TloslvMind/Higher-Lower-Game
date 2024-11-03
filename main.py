from art import logo, vs
from game_data import famous_people
from random import choice
from functions import format_data, check_answer

print(logo)

game_should_continue = True
account_b = choice(famous_people)

score = 0

while game_should_continue:
    account_a = account_b
    account_b = choice(famous_people)

    if account_a == account_b:
        account_b = choice(famous_people)

    print(f"Compare A: {format_data(account_a)}.\n")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    print('\n' * 20)

    follower_count_a = account_a['follower count']
    follower_count_b = account_b['follower count']

    is_correct = check_answer(answer, follower_count_a, follower_count_b)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}.")
        game_should_continue = False