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

    # 1 = True
    while 1:  # (while condition True, Python running the block below)
        print("infinite")


def condition_in_for():
    for i in range(6):
        if i == 2:
            pass
        # or, and
        # elif i == 2:
        #     continue
        elif i == 0 or i == 3:
            continue
        elif i == 4:
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
    # static vars
    # class vars
    # leg_num = 2

    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name
        self.name_age_mixin = name + "_" + str(age)  # "nathan_24"
        print("private age:", self.__get_age())

    # public will be inherited
    def get_age(self):
        return self.age

    def hello(self):
        return "hi, " + self.name

    # protected will be inherited
    def _get_age(self):
        return self.age

    # private will not be inherited
    def __get_age(self):
        return self.age

# instance()


class Female(Human):
    pass


class Male(Human):
    pass


def main():
    print(power(2, 3))
    for_in_range()
    for_in_range_params()
    condition_in_for()

    female = Female(age=1, name="kik")
    print("age:", female.age)
    print("age:", female.get_age())
    print("age:", female.__get_age())


if __name__ == "__main__":
    main()
