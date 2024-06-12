# No docstring here since this is a private module. Its members are
# exposed directly through the foo package.
# `__all__` can be used to control which members are documented.

__all__ = ("foobar",)


def undoc():
    """This function won't get documented.

    Since `undoc` is not in `__all__`, it won't be documented.
    """


def foobar(foo: str, bar: str) -> str:
    """Combine foo and bar.

    Args:
        foo: Left string.
        bar: Right string.

    Returns:
        A string combining the inputs.
    """
    return foo + bar
