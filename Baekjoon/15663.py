from sys import stdin


def recur(listed: list, m: int):
    pick = []
    size = len(listed)
    visit = [False] * size
    dict = {}

    def combination():
        pick_data = ' '.join(map(str, pick))
        if len(pick) == m:
            dict[pick_data] = 1
        else:
            for i in range(size):
                if visit[i] == True:
                    continue
                pick.append(listed[i])
                visit[i] = True
                combination()
                visit[i] = False
                pick.pop()

    combination()
    for key, item in dict.items():
        print(key)


def solution():
    n, m = map(int, stdin.readline().split())
    input_list = list(map(int, stdin.readline().split()))
    recur(sorted(input_list), m)


solution()
