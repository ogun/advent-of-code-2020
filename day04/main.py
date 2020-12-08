import re

import day04.data as data


def part1():
    value = data.INPUT

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_passport_count = 0
    for passport in value:
        key_value_pairs = passport.split()

        keys = {key_value.split(":")[0] for key_value in key_value_pairs}
        intersection = required_fields.intersection(keys)

        if intersection == required_fields:
            valid_passport_count += 1

    return valid_passport_count


def part2():
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

    value = data.INPUT

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
