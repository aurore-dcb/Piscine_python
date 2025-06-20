def square(x: int | float) -> int | float:
    """Returns the square of x."""
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an int or a float.")
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the power of x."""
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be an int or a float.")
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns an object that when called returns the result \
        of the arguments calculation."""
    count = 0

    def inner() -> float:
        """Applies the function to x and increments the count."""
        nonlocal count
        res = x
        for i in range(count + 1):
            res = function(res)
        count += 1
        return res

    return inner
