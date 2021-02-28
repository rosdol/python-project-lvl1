# -*- coding:utf-8 -*-

"""A file with functions ."""

import prompt


def welcome_user():
    """Asks the user for a name and welcomes him."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
