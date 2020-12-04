import functools
import itertools
import operator
import re

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


def day4_part1():
    value = data.day4.INPUT

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_passport_count = 0
    for passport in value:
        key_value_pairs = passport.split()

        keys = {key_value.split(":")[0] for key_value in key_value_pairs}
        intersection = required_fields.intersection(keys)

        if intersection == required_fields:
            valid_passport_count += 1

    return valid_passport_count


def day4_part2():
    rules = {
        "byr": {"regex": r"^[0-9]{4}$", "min": 1920, "max": 2002},
        "iyr": {"regex": r"^[0-9]{4}$", "min": 2010, "max": 2020},
        "eyr": {"regex": r"^[0-9]{4}$", "min": 2020, "max": 2030},
        "hgt": {
            "regex": r"^([0-9]+)(cm|in)$",
            "cm": {"min": 150, "max": 193},
            "in": {"min": 59, "max": 76},
        },
        "hcl": {"regex": r"^#[0-9a-f]{6}$"},
        "ecl": {"regex": r"^(amb|blu|brn|gry|grn|hzl|oth)$"},
        "pid": {"regex": r"^[0-9]{9}$"},
        "cid": {"regex": r"."},
    }

    value = data.day4.INPUT

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_passport_count = 0
    for passport in value:
        key_value_pairs = passport.split()

        keys = {key_value.split(":")[0] for key_value in key_value_pairs}
        intersection = required_fields.intersection(keys)

        if intersection != required_fields:
            continue

        valid = True
        for key_value in key_value_pairs:
            key = key_value.split(":")[0]
            value = key_value.split(":")[1]

            pattern = rules[key]["regex"]
            match = re.search(pattern, value)
            if not match:
                valid = False
                break

            if "max" in rules[key]:
                if not (rules[key]["max"] >= int(value) >= rules[key]["min"]):
                    valid = False
                    break

            if "cm" in rules[key]:
                val = match.group(1)
                typ = match.group(2)
                if not (rules[key][typ]["max"] >= int(val) >= rules[key][typ]["min"]):
                    valid = False
                    break

        if valid:
            valid_passport_count += 1

    return valid_passport_count
