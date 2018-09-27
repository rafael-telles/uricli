#!/usr/bin/env python3

"""
URI Online Judge Command Line Interface

Usage:
  uri.py login
  uri.py set_language
  uri.py submit <solution_path> [<problem_id>]
  uri.py (-h | --help)

Options:
  -h --help     Show this screen.

"""

from docopt import docopt
from PyInquirer import prompt

import lib


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
    solution_path = arguments["<solution_path>"]
    problem_id = arguments["<problem_id>"]

    lib.submit(solution_path, problem_id)


if __name__ == "__main__":
    arguments = docopt(__doc__)
    if arguments["login"]:
        cmd_login()
    elif arguments["set_language"]:
        cmd_set_language()
    elif arguments["submit"]:
        cmd_submit(arguments)
