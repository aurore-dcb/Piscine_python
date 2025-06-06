from S1E9 import Stark
# from S1E9 import Character


def main():

    # hodor = Character("hodor")

    c = Stark("Ned")
    print(c.__dict__)
    print(c.is_alive)
    c.die()
    print(c.is_alive)
    print(c.__doc__)
    print(c.__init__.__doc__)
    print(c.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    return


if __name__ == "__main__":
    main()
