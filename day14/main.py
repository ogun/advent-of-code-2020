import day14.data as data


def part1():
    value = data.INPUT

    def calculate_value(mask, base_value):
        binary = f"{base_value:b}".zfill(len(mask))

        result = ""
        for idx in range(len(mask)):
            m = mask[idx]
            if m in ["0", "1"]:
                result += m
            else:
                result += binary[idx]

        return int(result, 2)

    memory = {}
    for step in value:
        mask = step[0]
        instructions = step[1]

        for instruction in instructions:
            idx = instruction[0]
            base_value = instruction[1]

            real_value = calculate_value(mask, base_value)
            memory[idx] = real_value

    return sum(memory.values())


def part2():
    value = data.INPUT

    def replace_floating_bit(v):
        result = []

        v0 = v.replace("X", "0", 1)
        v1 = v.replace("X", "1", 1)

        if v0.count("X") == 0:
            result.extend([v0, v1])
            return result

        result.extend(replace_floating_bit(v0))
        result.extend(replace_floating_bit(v1))

        return result

    def calculate_idx_list(mask, base_value):
        binary = f"{base_value:b}".zfill(len(mask))

        result = ""
        for idx in range(len(mask)):
            m = mask[idx]
            if m == "1":
                result += m
            elif m == "0":
                result += binary[idx]
            else:
                result += "X"

        results = []
        results.extend(replace_floating_bit(result))

        return (int(r, 2) for r in results)

    memory = {}
    for step in value:
        mask = step[0]
        instructions = step[1]

        for instruction in instructions:
            idx = instruction[0]
            base_value = instruction[1]

            idx_list = calculate_idx_list(mask, idx)
            for idx in idx_list:
                memory[idx] = base_value

    return sum(memory.values())
