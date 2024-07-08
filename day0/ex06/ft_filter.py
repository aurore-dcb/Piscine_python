def ft_filter(fct, iterable):
    """Return an iterator yielding those items of iterable for which \
function(item)\nis true. If function is None, return the items that \
are true. """
    if fct is None:
        fct = bool
    res = (item for item in iterable if fct(item))
    if (isinstance(iterable, list)):
        return list(res)
    elif (isinstance(iterable, tuple)):
        return tuple(res)
    elif (isinstance(iterable, set)):
        return set(res)
    elif (isinstance(iterable, dict)):
        return {key: iterable[key] for key in iterable if fct(iterable[key])}
    else:
        return res


def doTests():
    """ Run the test cases for ft_filters(). """
    print("Test cases for ft_filter ...")
    try:
        assert ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4]) == [2, 4], \
            "Test case 1 failed"
        assert ft_filter(lambda x: x % 2 == 0, (1, 2, 3, 4)) == (2, 4), \
            "Test case 3 failed"
        assert ft_filter(lambda x: x % 2 == 0, {1, 2, 3, 4}) == {2, 4}, \
            "Test case 4 failed"
        assert ft_filter(lambda x: x > 1, {'a': 1, 'b': 2, 'c': 3}) == \
            {'b': 2, 'c': 3}, "Test case 5 failed"
        assert ft_filter(None, [1, 2, 3, 4]) == [1, 2, 3, 4], \
            "Test case 6 failed"
        assert ft_filter(None, [1, 2, 0, 4]) == [1, 2, 4], "Test case 7 failed"
        print("All test cases passed.")
    except AssertionError as msg:
        print("AssertionError:", msg)


# if __name__ == "__main__":
#     doTests()
