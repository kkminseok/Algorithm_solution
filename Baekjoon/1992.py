from sys import stdin

result = []


def recur(maps, row, col, size):
    def is_full(maps, row, col, size):
        bit = maps[row][col]
        for i in range(row, row + size):
            for j in range(col, col + size):
                if bit != maps[i][j]:
                    return False
        return True

    if is_full(maps, row, col, size):
        result.append(maps[row][col])
        return

    new_size = size // 2
    result.append('(')
    recur(maps, row, col, new_size)
    recur(maps, row, col + new_size, new_size)
    recur(maps, row + new_size, col, new_size)
    recur(maps, row + new_size, col + new_size, new_size)
    result.append(')')

def solution():
    size = int(stdin.readline())
    maps = []
    for _ in range(size):
        maps.append(stdin.readline().rstrip('\n'))
    recur(maps, 0, 0, size)
    print(''.join(result))

solution()
