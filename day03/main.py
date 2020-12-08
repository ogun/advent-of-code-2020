import functools
import operator

import day03.data as data


def part1():
    value = data.INPUT
    mod = len(value[0])

    tree_idx = 0
    tree_count = 0

    row_count = len(value)
    for row_idx in range(row_count):
        tree_idx = row_idx * 3

        if value[row_idx][tree_idx % mod] == "#":
            tree_count += 1

    return tree_count


def part2():
    value = data.INPUT
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
