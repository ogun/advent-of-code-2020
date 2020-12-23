import day23.data as data


def part1():
    value = data.INPUT

    def rotate(arr):
        return arr[1:] + arr[:1]

    def step(arr, current_idx):
        length = 9
        value = arr[current_idx]
        next_three = (arr + arr)[current_idx + 1 : current_idx + 4]

        rest = [x for x in arr if x not in next_three]

        destination = value - 1 if value - 1 > 0 else (value - 2) % (length + 1)
        while destination in next_three:
            destination = (
                destination - 1
                if destination - 1 > 0
                else (destination - 2) % (length + 1)
            )

        destination_idx = rest.index(destination)
        for i in range(3):
            rest.insert(destination_idx + (i + 1), next_three[i])

        while (value_idx := rest.index(value)) != current_idx:
            rest = rotate(rest)

        return rest

    for i in range(100):
        value = step(value, i % len(value))

    one_idx = value.index(1)
    result_arr = value[one_idx + 1 :] + value[:one_idx]

    return "".join((str(x) for x in result_arr))


def part2():
    value = data.INPUT
    value += range(10, 1000001)

    value_len = len(value)

    linked_list = {}
    for i in range(value_len - 1):
        linked_list[value[i]] = value[i + 1]
    linked_list[value[value_len - 1]] = value[0]

    current = value[0]
    for _ in range(10000000):
        next_1 = linked_list[current]
        next_2 = linked_list[next_1]
        next_3 = linked_list[next_2]
        linked_list[current] = linked_list[next_3]

        destination = (
            current - 1 if current - 1 > 0 else (current - 2) % (value_len + 1)
        )
        while destination in [next_1, next_2, next_3]:
            destination = (
                destination - 1
                if destination - 1 > 0
                else (destination - 2) % (value_len + 1)
            )

        linked_list[next_3] = linked_list[destination]
        linked_list[destination] = next_1
        current = linked_list[current]

    next_to_one = linked_list[1]
    second_next_to_one = linked_list[next_to_one]

    return next_to_one * second_next_to_one
