#!/usr/bin/env python

"""Basic code package."""

from brain_games.scripts import cli


def main():
    """Run an game code."""
    print('Welcome to the Brain Games!')
    cli.welcome_user()


if __name__ == '__main__':
    main()
