from functools import reduce
from operator import mul

import day16.data as data


def part1():
    value = data.INPUT

    min_value = min(r[0][0] for r in value["rules"].values())
    max_value = max(r[1][1] for r in value["rules"].values())

    result = sum(
        i for x in value["other_tickets"] for i in x if i > max_value or min_value > i
    )

    return result


def part2():
    value = data.INPUT

    min_value = min(r[0][0] for r in value["rules"].values())
    max_value = max(r[1][1] for r in value["rules"].values())

    invalid_tickets = [
        idx
        for idx, x in enumerate(value["other_tickets"])
        for i in x
        if i > max_value or min_value > i
    ]

    valid_tickets = [
        t for idx, t in enumerate(value["other_tickets"]) if idx not in invalid_tickets
    ]

    possibilities = {}
    field_len = len(value["my_ticket"])
    for rx in value["rules"]:
        r = value["rules"][rx]

        options = []
        for i in range(field_len):
            invalid_fields = list(
                t
                for t in valid_tickets
                if not (r[0][1] >= t[i] >= r[0][0] or r[1][1] >= t[i] >= r[1][0])
            )
            if invalid_fields:
                continue

            options.append(i)

        possibilities[rx] = options

    while any(True for p in possibilities if len(possibilities[p]) != 1):
        certain_values = [
            possibilities[p][0] for p in possibilities if len(possibilities[p]) == 1
        ]

        for certain_value in certain_values:
            for p_key in possibilities:
                if (
                    certain_value in possibilities[p_key]
                    and len(possibilities[p_key]) != 1
                ):
                    possibilities[p_key].remove(certain_value)

    target_values = [
        value["my_ticket"][possibilities[key][0]]
        for key in possibilities
        if key.startswith("departure ")
    ]

    return reduce(mul, target_values, 1)
