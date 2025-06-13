def ft_filter(fct, iterable):
    """ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which \
function(item)\nis true. If function is None, return the items that \
are true. """
    if fct is None:
        fct = bool
    res = (item for item in iterable if fct(item))
    return res


def doTests():
    """ Run the test cases for ft_filters(). """
    print("Test cases for ft_filter ...")

    print(list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
    print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])))
    print("-")
    print(list(ft_filter(lambda x: x % 2 != 0, [1, 2, 3, 4])))
    print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4])))
    print("-")
    print(list(ft_filter(lambda x: x % 2 == 0, {1, 2, 3, 4})))
    print(list(filter(lambda x: x % 2 == 0, {1, 2, 3, 4})))
    print("-")
    print(list(ft_filter(None, {0, 1, 2, 0, 3, 4})))
    print(list(filter(None, {0, 1, 2, 0, 3, 4})))


# if __name__ == "__main__":
#     # print("------------------------")
#     # print(filter.__doc__)
#     # print("------------------------")
#     # print(ft_filter.__doc__)
#     # print("------------------------")
#     doTests()
