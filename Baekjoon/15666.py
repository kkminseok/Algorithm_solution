from sys import stdin


def recur(data_list: list, size: int):
    pick = []
    pick_dict = {}

    def get_solution():
        if len(pick) == size:
            pick_dict[' '.join(map(str, pick))] = 1
        else:
            for i in range(len(data_list)):
                if len(pick) != 0 and (pick[-1] > data_list[i]):
                    continue
                pick.append(data_list[i])
                get_solution()
                pick.pop()

    get_solution()
    for key, value in pick_dict.items():
        print(key)


def solution():
    n, m = map(int, stdin.readline().split())
    input_list = list(map(int, stdin.readline().split()))

    recur(sorted(input_list), m)


solution()
