from sys import stdin


def solution():
    n, m = map(int, stdin.readline().split())
    input_list = list(map(int, stdin.readline().split()))
    for i in range(1,len(input_list)):
        input_list[i] += input_list[i-1]

    for _ in range(m):
        start, end = map(int,stdin.readline().split())
        if start == 1:
            print(input_list[end-1])
        else:
            print(input_list[end-1] - input_list[start-2])


solution()
