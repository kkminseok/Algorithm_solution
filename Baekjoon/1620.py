from sys import stdin


def solution() -> None:
    name_dict = {}
    number_dict = {}
    poketmon_list_size, output_len = map(int, stdin.readline().split())

    for i in range(1, poketmon_list_size + 1):
        poketmon_name = stdin.readline().rstrip('\n')
        name_dict[poketmon_name] = i
        number_dict[i] = poketmon_name

    for i in range(output_len):
        get_data = stdin.readline().rstrip('\n')
        if get_data.isdigit():
            print(number_dict.get(int(get_data)))
        else:
            print(name_dict.get(get_data))


solution()
