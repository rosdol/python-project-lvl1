#!/usr/bin/env python

"""Script."""

import random

import prompt
from brain_games.scripts import cli


def random_question():
    """Generate a question (random number)."""
    min_number = 0
    max_number = 20
    return random.randint(min_number, max_number)


def even_game(name):
    """Count the number of correct answers and announce the victory."""
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_of_win = 0
    while num_of_win != 3:
        question = random_question()
        print('Question: {0}'.format(question))
        answer = prompt.string('Your answer: ')
        test = is_right_answer(question, answer)
        if test is True:
            num_of_win += 1
        else:
            print("Let's try again, {0}!".format(name))
            break
    if num_of_win == 3:
        print('Congratulations, {0}!'.format(name))


def is_even(number):
    """Check the even number."""
    return number % 2 == 0


def answer_in_bool(answer):
    """Translate answer in a boolean."""
    return answer == 'yes'


def is_right_answer(question, answer):
    """Check that answer is correct."""
    if answer_in_bool(answer) == is_even(question):
        print('Correct!')
        return True
    elif answer_in_bool(answer) == is_even(question):
        print('Correct!')
        return True
    wrong_answer(answer)


def wrong_answer(answer):
    """Answer on wrong answer."""
    if answer == 'yes':
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
    if answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")


def main():
    """Run an game code."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
