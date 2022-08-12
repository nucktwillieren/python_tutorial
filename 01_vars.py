def main():
    print("hello, world")  # print a string

    print(1..is_integer())  # interger object

    print("hello, world".replace("e", "b"))  # string object

    # forbidden: o, O, I, l

    print(1 + 1)  # 2

    print(1 * 2)  # 2

    print(2 ** 3)  # 8

    print(2 / 3)  # 0.666666666666 round-off error vs truncation error
    # ieee 754
    # 大數相除以整數解

    print(3 / 2)  # 1.5

    print(3 // 2)  # 1

    print(float(1).is_integer())  # true

    print(float(1.).is_integer())  # true

    print(float(1.0).is_integer())  # true

    print(float(1.1).is_integer())  # false

    print(",".join(["1", "2", "3", "4"]))  # "1,2,3,4"

    print("c".replace("c", "d"))  # d

    print("efg".startswith("f"))  # false

    print("hi".endswith("i"))  # true

    print(" hi ".rstrip())  # hi

    print(" hi ".lstrip())  # hi

    print(" hi ".strip())  # hi

    print("1,2,3,4".split(","))  # ['1', '2', '3', '4']

    print("hi".upper())  # HI

    print("HI".lower())  # hi

    print("hi".capitalize())  # Hi

    print("a" + "b")  # ab

    print([1, 2, 3, 4, 5])  # list
    # list -> dynamic
    # array -> static

    print((1, 2, 3, 4))  # tuple
    # tuple -> immutable
    # list -> mutable

    print({
        "a": "b",
        "c": "d",
    })
    # dictionary -> dict
    # T: O(1) -> access, update, insert, delete (average)
    # T: O(n) -> get index by get()


if __name__ == "__main__":
    main()
