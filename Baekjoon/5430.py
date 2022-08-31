from collections import deque
from sys import stdin


def solution() -> None:
    t_case = int(stdin.readline())
    for _ in range(t_case):
        func = stdin.readline().rstrip('\n')
        size = int(stdin.readline().rstrip('\n'))
        data_list = stdin.readline().rstrip('\n').strip("[]")
        if data_list:
            data_list = deque(map(int, data_list.split(',')))
        # cnt == True -> R이 짝수번
        cnt = True
        error = False
        for i in range(len(func)):
            if func[i] == 'R':
                cnt = not cnt
            else:
                if cnt:
                    if data_list:
                        data_list.popleft()
                    else:
                        print('error')
                        error = not error
                        break
                else:
                    if data_list:
                        data_list.pop()
                    else:
                        print('error')
                        error = not error
                        break
        if not error:
            if cnt:
                print('[' + ','.join(map(str,data_list)) + ']')
            else:
                print('['+','.join(map(str,list(reversed(data_list)))) + ']')


solution()
