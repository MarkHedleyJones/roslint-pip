#!/usr/bin/env python

import sys

try:
    from roslint import pep8
except ImportError:
    # Allows the target to work with an un-sourced workspace.
    import os.path
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src"))
    from roslint import pep8


def main():
    # Prepend max line-length so that user can overide it. The number is 1
    # since 0 is the name of the program.
    sys.argv.insert(1, "--max-line-length=120")
    pep8._main()


if __name__ == '__main__':
    main()
