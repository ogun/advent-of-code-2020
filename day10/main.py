import day10.data as data


def part1():
    value = data.INPUT

    # The charging outlet & built-in joltage adapter
    value = [0, *value, max(value) + 3]

    one = sum(1 for idx in range(len(value) - 1) if value[idx + 1] - value[idx] == 1)
    three = sum(1 for idx in range(len(value) - 1) if value[idx + 1] - value[idx] == 3)

    return one * three


def part2():
    value = data.INPUT

    # The charging outlet & built-in joltage adapter
    value = [0, *value, max(value) + 3]

    max_value = max(value)

    cache = {}

    def depth_first(start, value):
        if start == max_value:
            return 1

        result = 0
        for i in range(1, 4):
            new_start = start + i

            if new_start in cache:
                result += cache[new_start]
            elif new_start in value:
                result += depth_first(new_start, value)

        cache[start] = result

        return result

    depth_first(0, value)

    return cache[0]
