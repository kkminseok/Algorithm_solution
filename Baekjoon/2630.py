from sys import stdin
from collections import deque

blue = 0
white = 0


def divide(maps, row, col, size):
    def is_full(maps, row, col, size):
        color = maps[row][col]
        for i in range(row, row + size):
            for j in range(col, col + size):
                print(i,j,size)
                if color != maps[i][j]:
                    return False
        return True

    if is_full(maps, row, col, size):
        if maps[row][col] == 0:
            global white
            white += 1
        else:
            global blue
            blue += 1
        return

    new_size = size // 2
    divide(maps, row, col, new_size)
    divide(maps, row, col + new_size, new_size)
    divide(maps, row + new_size, col, new_size)
    divide(maps, row + new_size, col + new_size, new_size)


def solution():
    n = int(stdin.readline())
    maps = deque()
    for i in range(n):
        maps.append(list(map(int, stdin.readline().split())))
    divide(maps, 0, 0, n)
    print(white, blue, sep='\n')


solution()
