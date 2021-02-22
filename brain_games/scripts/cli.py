# -*- coding:utf-8 -*-

"""Script."""

import prompt


def welcome_user():
    """Asks the user for a name and welcomes him."""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
