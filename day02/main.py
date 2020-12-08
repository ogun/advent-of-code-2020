import day02.data as data


def part1():
    value = data.INPUT

    result = 0
    for part in value:
        char = part[0]
        start = part[1]
        end = part[2]
        text = part[3]

        if end >= text.count(char) >= start:
            result += 1

    return result


def part2():
    value = data.INPUT

    result = 0
    for part in value:
        char = part[0]
        start = part[1] - 1
        end = part[2] - 1
        inp = part[3]

        text = inp[start] + inp[end]
        if text.count(char) == 1:
            result += 1

    return result
