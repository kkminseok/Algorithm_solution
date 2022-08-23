from sys import stdin
from heapq import heappop, heappush


def solution():
    n = int(stdin.readline())
    heap = []
    for i in range(n):
        command = int(stdin.readline())
        if command == 0:
            if len(heap) == 0:
                print(0)
            else:
                print(heappop(heap))
        else:
            heappush(heap, command)


solution()
