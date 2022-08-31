import heapq
from heapq import heappop, heappush
from sys import stdin


def solution() -> None:
    t = int(stdin.readline())
    for i in range(t):
        command_count = int(stdin.readline())
        max_heap = []
        min_heap = []
        dic = {}
        for _ in range(command_count):
            command, data = map(str, stdin.readline().split())
            data = int(data)
            # print(command, data, dic)
            if command == 'I':
                heapq.heappush(max_heap, -data)
                heapq.heappush(min_heap, data)
                if data in dic:
                    dic[data] += 1
                else:
                    dic[data] = 1
            else:
                if data == -1:
                    while min_heap:
                        root = heappop(min_heap)
                        if dic[root] != 0:
                            dic[root] -= 1
                            break
                else:
                    while max_heap:
                        root = -heapq.heappop(max_heap)
                        if dic[root] != 0:
                            dic[root] -= 1
                            break
        while max_heap and dic[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        while min_heap and dic[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        if max_heap:
            print(-max_heap[0], min_heap[0])
        else:
            print("EMPTY")


solution()
