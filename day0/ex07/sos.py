import sys

NESTED_MORSE = {" ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
                "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
                "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
                "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
                "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
                "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                "6": "-....", "7": "--...", "8": "---..", "9": "----. "
                }


def main():
    try:
        assert len(sys.argv) == 2
        assert type(sys.argv[1]) is str
        assert all(c.isalnum() or c == ' ' for c in sys.argv[1])

        S = sys.argv[1].upper()
        res = ' '.join(NESTED_MORSE[c] for c in S)
        print(res)
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
