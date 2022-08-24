from sys import stdin


def solution():
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        dict = {}
        result = 1
        for k in range(n):
            name, type = list(map(str, stdin.readline().split()))
            if type not in dict:
                dict[type] = []
            dict[type].append(name)

        for key, value in dict.items():
            result *= (len(value) + 1)
        print(result - 1)


solution()
