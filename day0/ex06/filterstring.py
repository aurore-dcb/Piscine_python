import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3, "only one argument is provided"
        assert type(sys.argv[1]) is str, \
            "argument 1 is not a string"
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1]), \
            "argument 1 contains forbidden characters"
        assert sys.argv[2].lstrip('-').isdigit(), \
            "argument 2 is not an integer"

        S = sys.argv[1]
        N = int(sys.argv[2])
        words_list = S.split()
        res = ft_filter(lambda x: len(x) > N, words_list)
        print(res)
    except AssertionError:
        print("AssertionError:", "the arguments are bad")
        return


if __name__ == "__main__":
    main()
