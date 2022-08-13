def main():
    arr = []
    n = int(input("n: "))
    
    while n != 0:
        arr.insert(0, str(n % 2))
        n = n // 2

    print("List format: ", arr)
    print("Str  format: ", "".join(arr))

if __name__ == "__main__":
    main()