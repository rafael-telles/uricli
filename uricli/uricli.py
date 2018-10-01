#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""URI Online Judge Command Line Interface

Usage:
  uri login
  uri set_language
  uri submit <solution_path> [<problem_id>]
  uri live

Arguments
    <solution_path>     Path to the file containing to solution.
    <problem_id>        URI Online Judge's problem ID

"""

from docopt import docopt
from PyInquirer import prompt


from . import lib
from .live import LiveSession


__version__ = "0.2.1"


def cmd_login():
    questions = [
        {
            'type': 'input',
            'name': 'email',
            'message': 'Email',
        }, {
            'type': 'password',
            'name': 'password',
            'message': 'Password',
        }
    ]
    answers = prompt(questions)

    lib.set_login(answers["email"], answers["password"])


def cmd_set_language():
    language_map = {text: id for (id, text) in lib.list_languages()}

    questions = [
        {
            'type': 'list',
            'name': 'language_key',
            'message': 'Language',
            'choices': language_map.keys()
        }
    ]
    answers = prompt(questions)
    language_key = answers['language_key']
    language_id = language_map[language_key]

    lib.set_language(language_id)


def cmd_submit(arguments):
    try:
        lib.get_language()
    except:
        cmd_set_language()  # Ensure language is set first

    solution_path = arguments["<solution_path>"]
    problem_id = arguments["<problem_id>"]

    lib.submit(solution_path, problem_id)


def cmd_live():
    session = LiveSession()
    session.run()


def cmd_help():
    print(__doc__)


def main():
    try:
        arguments = docopt(__doc__, help=False, version=__version__)
    except SystemExit:
        cmd_help()
        exit(1)
        return

    try:
        if arguments["login"]:
            cmd_login()
        elif arguments["set_language"]:
            cmd_set_language()
        elif arguments["submit"]:
            cmd_submit(arguments)
        elif arguments["live"]:
            cmd_live()
        else:
            cmd_help()
    except Exception as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
