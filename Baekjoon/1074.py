from sys import stdin


def solution():
    n, r, c = map(int, stdin.readline().split())
    size = 1
    for i in range(n):
        size *= 2
    result = x = y = 0
    while size != 0:
        size //= 2
        if r < x + size and c < y + size:
            result += 0
        elif r < x + size and c >= y + size:
            result += size * size * 1
            y += size
        elif r >= x + size and c < y + size:
            result += size * size * 2
            x += size
        else:
            result += size * size * 3
            x += size
            y += size

        if size == 1:
            print(result)


solution()
