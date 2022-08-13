
def long_division(n, d, precision):
    t = n
    integer = 0
    float_nums = ""
    for i in range(precision+1):
        q = n // d
        r = n % d
        reminder = r / 10**i
        if i == 0: 
            integer = q
        else:
            float_nums += str(q)
        print(f"{t} / {d} = {integer}.{float_nums} (remainder: {reminder})")
        n = r * 10 
    return float(f"{integer}.{float_nums}")

def main():
    n = int(input("n(ex: 20): "))
    d = int(input("divider(ex: 7): "))
    p = int(input("precision(ex: 10): "))

    result = long_division(n, d, p)
    print(f"result: {result}")

if __name__ == '__main__':
    main()
    