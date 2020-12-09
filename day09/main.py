import itertools

import day09.data as data


def part1():
    value = data.INPUT

    for idx in range(25, len(value)):
        pre_25 = value[idx - 25 : idx]
        sums = [sum(pair) for pair in itertools.permutations(pre_25, 2)]

        current = value[idx]

        if current not in sums:
            return current

    return 0


def part2():
    value = data.INPUT

    target = 29221323
    for start_idx in range(len(value)):
        for item_count in range(2, len(value) - start_idx):
            items = []
            for idx in range(item_count):
                items.append(value[start_idx + idx])

            total = sum(items)
            if total == target:
                return min(items) + max(items)

            if total > target:
                break

    return 0
