import sys

len = len(sys.argv)
try:
    assert len <= 2, "more than one argument is provided"
    if (len == 2):
        if sys.argv[1].startswith('-') or sys.argv[1].startswith('+'):
            sys.argv[1] = sys.argv[1][1:]
        assert sys.argv[1].isdigit(), "argument is not an integer"
        if (int(sys.argv[1]) % 2 == 0):
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as msg:
    print("AssertionError:", msg)
