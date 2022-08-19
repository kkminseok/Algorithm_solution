from operator import itemgetter
from sys import stdin


# noinspection PyTupleAssignmentBalance
def solution() -> None:
    def init():
        cnt = int(stdin.readline())
        input_list = []
        for i in range(cnt):
            input_list.append(int(stdin.readline()))
        return cnt, input_list

    def operation(li: list, counting_list: list):
        sum_ = 0
        max_ = 0
        for i in range(len(li)):
            sum_ += li[i]
            idx = li[i] + 4000
            counting_list[idx] += 1
            if max_ < counting_list[idx]:
                max_ = counting_list[idx]
        return sum_, max_

    counting = [0] * 8001
    max_list = []
    n, data_input = init()

    data_input.sort()

    data_sum, max_result = operation(data_input, counting)

    for i in range(len(counting)):
        if counting[i] == max_result:
            max_list.append(i)

    max_result = max_list[-1] if len(max_list) == 1 else max_list[1]
    print(round(data_sum / n), data_input[n // 2], max_result - 4000, data_input[-1] - data_input[0], sep='\n')


solution()
