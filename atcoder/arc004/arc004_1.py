import math


def main():
    n: int = int(input())
    x: List[int] = []
    y: List[int] = []
    for i in range(n):
        row: List[string] = input().split()
        x.append(int(row[0]))
        y.append(int(row[1]))
    distance: List[float] = []
    for i in range(n):
        for j in range(n):
            distance.append(calcDistance(x[i], y[i], x[j], y[j]))
    ans: float = max(distance)
    print(ans)


def calcDistance(fromX: int, fromY: int, toX: int, toY: int) -> float:
    return math.sqrt(float((fromX - toX)**2 + (fromY - toY)**2))


if __name__ == "__main__":
    main()
