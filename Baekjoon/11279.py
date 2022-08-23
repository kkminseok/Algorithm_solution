from heapq import heappush, heappop

from sys import stdin


def solution() -> None:
    n = int(stdin.readline())
    heap = []
    for i in range(n):
        command = int(stdin.readline())
        if command == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heappop(heap)[1])
        else:
            heappush(heap, (-command, command))


solution()
