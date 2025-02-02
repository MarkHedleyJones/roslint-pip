#!/usr/bin/env python

import sys

try:
    from roslint import cpplint_wrapper
except ImportError:
    # Allows the target to work with an un-sourced workspace.
    import sys, os.path
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src"))
    from roslint import cpplint_wrapper


def main():
    # Adding default flags to cpplint.
    # You can override them using global CMAKE variable ROSLINT_CPP_OPTS.
    # The index of injected argument is 1 because 0 is program's name
    sys.argv.insert(1, "--filter=-runtime/references")
    cpplint_wrapper.main()


if __name__ == '__main__':
    main()
