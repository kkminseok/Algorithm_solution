from sys import stdin


def row_sum(row: list) -> list:
    for i in range(1, len(row)):
        row[i] += row[i - 1]
    return row


def solution() -> None:
    n, m = map(int, stdin.readline().split())
    maps = []
    for i in range(n):
        row = list(map(int, stdin.readline().split()))
        row = row_sum(row)
        maps.append(row)
    for j in range(m):
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        result = 0
        for x in range(x1 - 1, x2):
            if y1 - 2 < 0:
                result += maps[x][y2 - 1]
            else:
                result += maps[x][y2 - 1] - maps[x][y1 - 2]
        print(result)


solution()
