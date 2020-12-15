import day15.data as data


def find_last_number(start_array, step):
    number = 0
    last_indexes = {}
    for i in range(step):
        if len(start_array) > i:
            number = start_array[i]
            last_indexes[number] = [i]
            continue

        index_list = last_indexes[number]
        if len(index_list) == 1:
            number = 0
        else:
            number = i - 1 - index_list[-2]

        if number in last_indexes:
            last_indexes[number].append(i)
        else:
            last_indexes[number] = [i]

    return number


def part1():
    value = data.INPUT

    return find_last_number(value, 2020)


def part2():
    value = data.INPUT

    return find_last_number(value, 30000000)
