import functools

import day06.data as data


def part1():
    value = data.INPUT

    total = 0
    for i in value:
        total += len(set(i))

    return total


def part2():
    value = data.INPUT2

    total = 0
    for inp in value:
        sets = [set(st) for st in inp]
        intersection = functools.reduce(set.intersection, sets)
        total += len(intersection)

    return total
