from heapq import heappush, heappop
from sys import stdin


def solution():
    command_line = int(stdin.readline())
    heap = []
    for _ in range(command_line):
        command = int(stdin.readline())
        if command == 0:
            if len(heap) != 0:
                print(heappop(heap)[1])
            else:
                print(0)
        else:
            heappush(heap, (abs(command), command))


solution()
