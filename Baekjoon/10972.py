def solution(origin, size):
    i = size - 1
    while i > 0 and origin[i - 1] >= origin[i]:
        i -= 1

    j = size - 1
    while origin[j] <= origin[i - 1]:
        j -= 1
    origin[i - 1], origin[j] = origin[j], origin[i - 1]

    j = size - 1
    while (i < j):
        origin[i], origin[j] = origin[j], origin[i]
        i += 1
        j -= 1
    print(' '.join(map(str, origin)))


n = int(input())
input_str = list(map(int, input().split()))
permu_list = [_x for _x in range(1, n + 1)]

if list(input_str)[::-1] == permu_list:
    print(-1)
else:
    size = len(permu_list)
    solution(input_str, size)
