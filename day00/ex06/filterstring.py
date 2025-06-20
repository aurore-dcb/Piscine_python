import sys
from ft_filter import ft_filter


def main():
    """ The program output a list of words from a given string S \
        that have a length greater than a given number N.
    """
    try:
        assert len(sys.argv) == 3
        assert type(sys.argv[1]) is str
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1])
        if sys.argv[2].startswith('-') or sys.argv[2].startswith('+'):
            arg = sys.argv[2][1:]
        else:
            arg = sys.argv[2]
        assert (arg.isdigit())
        assert int(sys.argv[2]) >= 0
    except AssertionError:
        print("AssertionError: the arguments are bad")
        return
    S = sys.argv[1]
    N = int(sys.argv[2])
    words_list = S.split()
    res = list(ft_filter(lambda x: len(x) > N, words_list))
    print(res)


if __name__ == "__main__":
    main()
