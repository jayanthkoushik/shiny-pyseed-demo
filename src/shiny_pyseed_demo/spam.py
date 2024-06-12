"""Module with a class."""


class Spam:
    #  Note: arguments for initialization should be documented here,
    #  rather than in `__init__`.
    """A spammer.

    Args:
        n: How many times to spam.

    Examples:
        >>> from shiny_pyseed_demo.spam import Spam
        >>> spammer = Spam(5)
        >>> spammer.spam()
        SPAM SPAM SPAM SPAM SPAM

    """

    def __init__(self, n: int):
        self.n = n

    def spam(self) -> None:
        print(" ".join(["SPAM"] * self.n))
