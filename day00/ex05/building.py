import sys


def main():
    """ This function reads a string from the command line or from the
        standard input and prints the number of characters, upper and lower
        letters, ponctuation marks, spaces and the number of digits in the
        string. """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if (len(sys.argv) == 1):
            print("What is the text to count?")
            str = sys.stdin.read()
        else:
            if (sys.argv[1] is None or sys.argv[1] == ""):
                print("What is the text to count?")
                str = sys.stdin.read()
            else:
                str = sys.argv[1]
        print("The text contains", len(str), "character(s):")
        print(sum(1 for c in str if c.isupper()), "upper letter(s)")
        print(sum(1 for c in str if c.islower()), "lower letter(s)")
        ponctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
        print(sum(1 for c in str if c in ponctuation), "ponctuation mark(s)")
        print(sum(1 for c in str if c.isspace()), "space(s)")
        print(sum(1 for c in str if c.isdigit()), "digit(s)")

    except AssertionError as msg:
        print("AssertionError:", msg)
        return


if __name__ == "__main__":
    main()
