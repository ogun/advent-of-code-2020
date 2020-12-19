from copy import copy
import re

import day19.data as data


def get_regex(rules):
    while re.search("[0-9]", rules[0]):
        matches = re.findall("[0-9]+", rules[0])
        for number in matches:
            old = r"\b{}\b".format(number)

            new_value = rules[int(number)]
            new = f"({new_value})" if "|" in new_value else new_value

            rules[0] = re.sub(old, new, rules[0], 1)

    pattern = rules[0].replace(" ", "")
    pattern = f"^{pattern}$"
    return re.compile(pattern)


def part1():
    value = data.INPUT
    rules = data.RULES

    r = get_regex(rules)

    return sum(1 for i in value if r.match(i))


def part2():
    value = data.INPUT
    rules = data.RULES

    last_total = 0
    max_range = max(len(v) for v in value) + 1
    for m_range in range(2, max_range):
        rule_8, rule_11 = [], []

        for i in range(1, m_range):
            rule_8.append("42 " * i)
            rule_11.append("42 " * i + "31 " * i)

        rules[8] = " | ".join(rule_8)
        rules[11] = " | ".join(rule_11)

        r = get_regex(copy(rules))

        total = sum(1 for i in value if r.match(i))

        if last_total != total:
            last_total = total
        else:
            return total

    return 0
