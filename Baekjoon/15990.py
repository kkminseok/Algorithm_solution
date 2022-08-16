from sys import stdin

mod = 1000000009
t = int(stdin.readline())

input_list = []
for i in range(t):
    input_list.append(int(stdin.readline()))
max_num = max(input_list) + 1

dp_one = [0] * max_num
dp_two = [0] * max_num
dp_three = [0] * max_num

dp_one[1] = 1
dp_one[3] = 1
dp_two[2] = 1
dp_two[3] = 1
dp_three[3] = 1

for i in range(4, max_num):
    dp_one[i] = (dp_two[i - 1] + dp_three[i - 1]) % mod
    dp_two[i] = (dp_one[i - 2] + dp_three[i - 2]) % mod
    dp_three[i] = (dp_one[i - 3] + dp_two[i - 3]) % mod

for result in input_list:
    print((dp_one[result] + dp_two[result] + dp_three[result]) % mod)
