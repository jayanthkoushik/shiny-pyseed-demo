"""This is a subpackage."""

from ._bar import *

# Note: we have to explicitly define `__all__` since this package does
# not have a public interface.
__all__ = _bar.__all__  # type: ignore
