import functools
import itertools
import operator

import data


def day1_part1():
    value = data.day1.INPUT
    pair = list(x for x in itertools.combinations(value, 2) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result


def day1_part2():
    value = data.day1.INPUT
    pair = list(x for x in itertools.combinations(value, 3) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result


def day2_part1():
    value = data.day2.INPUT

    result = 0
    for part in value:
        char = part[0]
        start = part[1]
        end = part[2]
        text = part[3]

        if end >= text.count(char) >= start:
            result += 1

    return result


def day2_part2():
    value = data.day2.INPUT

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
