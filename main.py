import copy
import functools
import itertools
import operator
import re

import data


def day01_part1():
    value = data.day01.INPUT
    pair = list(x for x in itertools.combinations(value, 2) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result


def day01_part2():
    value = data.day01.INPUT
    pair = list(x for x in itertools.combinations(value, 3) if sum(x) == 2020)
    result = functools.reduce(operator.mul, pair[0])
    return result


def day02_part1():
    value = data.day02.INPUT

    result = 0
    for part in value:
        char = part[0]
        start = part[1]
        end = part[2]
        text = part[3]

        if end >= text.count(char) >= start:
            result += 1

    return result


def day02_part2():
    value = data.day02.INPUT

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


def day03_part1():
    value = data.day03.INPUT
    mod = len(value[0])

    tree_idx = 0
    tree_count = 0

    row_count = len(value)
    for row_idx in range(row_count):
        tree_idx = row_idx * 3

        if value[row_idx][tree_idx % mod] == "#":
            tree_count += 1

    return tree_count


def day03_part2():
    value = data.day03.INPUT
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


def day04_part1():
    value = data.day04.INPUT

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_passport_count = 0
    for passport in value:
        key_value_pairs = passport.split()

        keys = {key_value.split(":")[0] for key_value in key_value_pairs}
        intersection = required_fields.intersection(keys)

        if intersection == required_fields:
            valid_passport_count += 1

    return valid_passport_count


def day04_part2():
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

    value = data.day04.INPUT

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


def day05_part1():
    value = data.day05.INPUT

    max_seat_id = 0
    for boarding_pass in value:
        seat_id = int(
            boarding_pass.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )
        max_seat_id = max(max_seat_id, seat_id)

    return max_seat_id


def day05_part2():
    value = data.day05.INPUT

    seat_ids = []
    for boarding_pass in value:
        seat_id = int(
            boarding_pass.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )
        seat_ids.append(seat_id)

    for seat_id in range(min(seat_ids), max(seat_ids) + 1):
        if seat_id not in seat_ids:
            return seat_id


def day06_part1():
    value = data.day06.INPUT

    total = 0
    for i in value:
        total += len(set(i))

    return total


def day06_part2():
    value = data.day06.INPUT2

    total = 0
    for inp in value:
        sets = [set(st) for st in inp]
        intersection = functools.reduce(set.intersection, sets)
        total += len(intersection)

    return total


def day07_part1():
    value = data.day07.INPUT

    def find_color(color, nodes):
        for node in nodes:
            node_color = node[1]

            if node_color == color:
                return True

            if find_color(color, value[node_color]):
                return True

        return False

    total = set()
    for color in value:
        node_item = value[color]

        has_color = find_color("shiny gold", node_item)
        if has_color:
            total.add(color)

    return len(total)


def day07_part2():
    value = data.day07.INPUT

    def bag_count(bags):
        total_bag = 0

        for bag in bags:
            total_bag += bag[0] + bag[0] * bag_count(value[bag[1]])

        return total_bag

    return bag_count(value["shiny gold"])


def day08_part1():
    value = data.day08.INPUT

    idx = 0

    result = 0
    visited = set()
    while True:
        instruction = value[idx][0]
        command = value[idx][1]

        idx += command if instruction == "jmp" else 1
        if instruction == "acc":
            result += command

        if idx in visited:
            return result

        visited.add(idx)

    return 0


def day08_part2():
    value = data.day08.INPUT

    permuatations = []
    jmp_idxs = [idx for idx, value in enumerate(value) if value[0] == "jmp"]
    for jmp_idx in jmp_idxs:
        new_arr = copy.deepcopy(value)
        new_arr[jmp_idx][0] = "nop"
        permuatations.append(new_arr)

    nop_idxs = [idx for idx, value in enumerate(value) if value[0] == "nop"]
    for nop_idx in nop_idxs:
        new_arr = copy.deepcopy(value)
        new_arr[nop_idx][0] = "jmp"
        permuatations.append(new_arr)

    for perm in permuatations:
        idx = 0
        result = 0
        visited = set()
        while True:
            instruction = perm[idx][0]
            command = perm[idx][1]

            if instruction == "acc":
                result += command

            if idx == len(perm) - 1:
                return result
            else:
                idx += command if instruction == "jmp" else 1

            if idx in visited:
                break

            visited.add(idx)

    return 0
