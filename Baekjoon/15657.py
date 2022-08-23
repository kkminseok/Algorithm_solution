from sys import stdin


def recur(num_list: list, m: int):
    pick = []

    def combination():
        if m == len(pick):
            print(' '.join(map(str, pick)))
        else:
            for i in range(len(num_list)):
                if len(pick) != 0 and (pick[-1] > num_list[i]):
                    continue
                pick.append(num_list[i])
                combination()
                pick.pop()

    combination()


def solution():
    n, m = map(int, stdin.readline().split())
    num_list = list(map(int, stdin.readline().split()))
    recur(sorted(num_list), m)


solution()
