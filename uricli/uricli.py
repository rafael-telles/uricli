#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
URI Online Judge Command Line Interface

Usage:
  uri login
  uri set_language
  uri submit <solution_path> [<problem_id>]
  uri (-h | --help)
  uri (-v | --version)

Options:
  -h --help      Show this screen.
  -v --version   Show version.

"""

from docopt import docopt
from PyInquirer import prompt

from . import lib


__version__ = "0.0.6"


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


def main():
    arguments = docopt(__doc__, version=__version__)
    if arguments["login"]:
        cmd_login()
    elif arguments["set_language"]:
        cmd_set_language()
    elif arguments["submit"]:
        cmd_submit(arguments)


if __name__ == "__main__":
    main()
