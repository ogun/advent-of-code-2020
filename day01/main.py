import itertools
import functools
import operator

import day01.data as data


def part1():
    value = data.INPUT
    pair = list(x for x in itertools.combinations(value, 2) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result


def part2():
    value = data.INPUT
    pair = list(x for x in itertools.combinations(value, 3) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result
