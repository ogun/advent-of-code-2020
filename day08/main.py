import copy

import day08.data as data


def part1():
    value = data.INPUT

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


def part2():
    value = data.INPUT

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
