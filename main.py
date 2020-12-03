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


def day3_part1():
    value = data.day3.INPUT
    mod = len(value[0])

    tree_idx = 0
    tree_count = 0

    row_count = len(value)
    for row_idx in range(row_count):
        tree_idx = row_idx * 3

        if value[row_idx][tree_idx % mod] == "#":
            tree_count += 1

    return tree_count


def day3_part2():
    value = data.day3.INPUT
    row_count = len(value)
    mod = len(value[0])

    slopes = [
        (1, 1),
        (1, 3),
        (1, 5),
        (1, 7),
        (2, 0.5),
    ]

    trees = []
    for slope in slopes:
        step = slope[0]
        right = slope[1]

        tree_idx = 0
        tree_count = 0
        for row_idx in range(0, row_count, step):
            tree_idx = int(row_idx * right)

            if value[row_idx][tree_idx % mod] == "#":
                tree_count += 1

        trees.append(tree_count)

    result = functools.reduce(operator.mul, trees)
    return result
