import math


def main():
    a: int
    b: int
    c: int
    a, b, c = map(int, input().split())
    print(det(a, b, c))
    print(solution1(a, b, c))
    print(solution2(a, b, c))


def det(a: int, b: int, c: int) -> float:
    return b ** 2 - 4 * a * c


def solution1(a: int, b: int, c: int) -> float:
    determinant: float = det(a, b, c)
    return (-b + math.sqrt(determinant)) / (a * 2)


def solution2(a: int, b: int, c: int) -> float:
    determinant: float = det(a, b, c)
    return (-b - math.sqrt(determinant)) / (a * 2)


if __name__ == "__main__":
    main()
