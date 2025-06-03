import sys
from ft_filter import ft_filter


def main():
    """ The program output a list of words from a given string S \
        that have a length greater than a given number N.
    """
    try:
        assert len(sys.argv) == 3, "expected 2 arguments, a string and a number"
        assert type(sys.argv[1]) is str, "first argument must be a string"
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1]), "first argument shouldn't contain special characters"
        if sys.argv[2].startswith('-') or sys.argv[2].startswith('+'):
            sys.argv[2] = sys.argv[2][1:]
        assert sys.argv[2].isdigit(), "second argument must be an integer" # nombre negatif ?
    except AssertionError as e:
        print("AssertionError:", "the arguments are bad:", e)
        return
    S = sys.argv[1]
    N = int(sys.argv[2])
    words_list = S.split()
    res = ft_filter(lambda x: len(x) > N, words_list)
    print(res)


if __name__ == "__main__":
    # print(ft_filter.__doc__)
    # print(filter.__doc__)
    main()
