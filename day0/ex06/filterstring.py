import sys
from ft_filter import ft_filter


def main():
    try:
        assert len(sys.argv) == 3
        assert type(sys.argv[1]) is str
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1])
        if sys.argv[2].startswith('-') or sys.argv[2].startswith('+'):
            sys.argv[2] = sys.argv[2][1:]
        assert sys.argv[2].isdigit()
    except AssertionError:
        print("AssertionError:", "the arguments are bad")
        return
    S = sys.argv[1]
    N = int(sys.argv[2])
    words_list = S.split()
    res = ft_filter(lambda x: len(x) > N, words_list)
    print(res)


if __name__ == "__main__":
    main()
