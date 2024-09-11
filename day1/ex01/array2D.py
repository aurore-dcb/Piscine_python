import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """ Print the shape of the given 2D array and returns a truncated \
        version of the array based on the provided start and end. """
    try:
        assert isinstance(family, list)
        assert all(len(sublist) == len(family[0]) for sublist in family)
        arr = np.array(family)
        assert arr.ndim == 2
        assert len(family) > 1
        assert type(start) is int and type(end) is int

        def absolute_index(i):
            if i < 0:
                i = len(family) + i
            return i

        start = absolute_index(start)
        end = absolute_index(end)
        assert start >= 0 and start < len(family)
        assert end >= 0 and end < len(family)
        assert start < end
    except AssertionError:
        print("AssertionError: bad argument")
        return
    print("My shape is :", arr.shape)
    new_arr = arr[start:end]
    print("My new shape is :", new_arr.shape)
    return new_arr.tolist()
