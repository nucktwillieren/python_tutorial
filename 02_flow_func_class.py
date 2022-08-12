from time import time


def multiply(a, b):
    return a * b


def power(base, exponent):
    a = 1
    for _ in range(exponent):
        a = a * base

    return a


def for_in_range():
    # range from 0 to 9
    for i in range(10):
        print(i, end=",")

    print()


def for_in_range_params():
    # range from 1 to 10 (11-1)
    for i in range(1, 11, 2):
        print(i, end=",")

    print()


def while_infinite_loop():
    # what are the boolean False Values in Python?
    # bool(False)
    # bool(None)
    # bool(0)
    # bool("")
    # bool(())
    # bool([])
    # bool({})

    while 1:  # (while condition True, Python running the block below)
        print("infinite")


def condition_in_for():
    for i in range(6):
        if i == 2:
            pass
        # or, and
        if i == 0 or i == 3:
            continue
        if i == 4:
            break
        print(i, end=",")

    print()

    for i in range(6):
        if i == 2:
            print("")
            return
        print(i, end=",")

    print("213455")  # early return


class Human:
    def __init__(self, age: int) -> None:
        self.age = age
        print("private age:", self.__get_age())

    # public will be inherited
    def get_age(self):
        return self.age

    # protectd will be inherited
    def _get_age(self):
        return self.age

    # private will not be inherited
    def __get_age(self):
        return self.age


class Person(Human):
    pass


def main():
    print(power(2, 3))
    for_in_range()
    for_in_range_params()
    condition_in_for()

    person = Person(age=1)
    print("age:", person.age)
    print("age:", person.get_age())
    print("age:", person.__get_age())


if __name__ == "__main__":
    main()
