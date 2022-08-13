
class Person:
    c = 1

    def __init__(self) -> None:
        pass
        # self.c = 3

    @classmethod
    def test(cls):
        cls.c


if __name__ == "__main__":
    p_a = Person()
    p_b = Person()

    p_a.c = 3

    print(p_a.c)
    print(p_b.c)

    p_a.__class__.c = 4
    print(p_a.__class__.c)
    print(p_b.__class__.c)
