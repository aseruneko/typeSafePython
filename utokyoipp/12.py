def main():
    f: int
    i: int
    a: int
    b: int
    c: int
    x: int
    f, i, a, b, c, x = map(int, [input() for _ in range(6)])
    print(feetToCm(f, i))
    print(quadratic(a, b, c, x))


def feetToCm(f: int, i: int) -> float:
    return(f + i / 12)*30.48


def quadratic(a: int, b: int, c: int, x: int) -> int:
    return a * (x ** 2) + b * x + c


if __name__ == "__main__":
    main()
