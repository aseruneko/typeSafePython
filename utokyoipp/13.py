def main():
    x: int
    y: int
    x, y = map(int, input().split())
    print(absolute(x))
    print(sign(y))


def absolute(x: int) -> int:
    if (x > 0):
        return x
    else:
        return -x


def sign(x: int) -> int:
    if (x > 0):
        return 1
    elif (x == 0):
        return 0
    else:
        return -1


if __name__ == "__main__":
    main()
