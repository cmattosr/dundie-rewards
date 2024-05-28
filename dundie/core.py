"""Core module of dundie"""

from dundie.utils.log import get_logger  # noqa


def load(filepath):
    """Loads data from filepath to the database
    doctest:
    >>> len(load("assets\people.csv")) # noqa
    2
    >>> load("assets\people.csv")[0][0]
    'J'
    """
    try:
        with open(filepath) as file_:
            # for line in file:
            #     print(line)
            return file_.readlines()
    except FileNotFoundError as e:
        # print(f"File not found {e}.")
        log.error(str(e))  # noqa
        raise e
