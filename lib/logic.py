import sys


def name_from_cli():
    """The invokers name is the first argument passed on the cli"""

    # Index out of rage error, try:
    # if len(sys.argv) > 1:
    #     then return sys.argv[1]
    # else:
    #     return "Some default value"

    return sys.argv[1]