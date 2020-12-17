import copy

import day17.data as data


def part1():
    value = data.INPUT

    def get_neigbours(col, row, layer, col_length, row_length, layer_length):
        neigbours = []

        for col_idx in range(col - 1, col + 2):
            for row_idx in range(row - 1, row + 2):
                for layer_idx in range(layer - 1, layer + 2):
                    if (
                        -1 in [col_idx, row_idx, layer_idx]
                        or col_idx == col_length
                        or row_idx == row_length
                        or layer_idx == layer_length
                    ):
                        continue

                    if (col, row, layer) == (col_idx, row_idx, layer_idx):
                        continue

                    neigbours.append((col_idx, row_idx, layer_idx))

        return neigbours

    def next_step(value):
        result = copy.deepcopy(value)

        for row_idx, row in enumerate(value):
            for col_idx, col in enumerate(row):
                for layer_idx, layer in enumerate(col):
                    current = value[row_idx][col_idx][layer_idx]

                    neigbours = get_neigbours(
                        col_idx,
                        row_idx,
                        layer_idx,
                        len(value[0]),
                        len(value),
                        len(value[0][0]),
                    )
                    lights_on = sum(
                        1 for n in neigbours if value[n[1]][n[0]][n[2]] == "#"
                    )

                    if current == "#" and lights_on not in [2, 3]:
                        result[row_idx][col_idx][layer_idx] = "."
                        continue

                    if current == "." and lights_on == 3:
                        result[row_idx][col_idx][layer_idx] = "#"
                        continue

        return result

    step = 6
    cube_length = step * 2 + len(value) + 1
    middle = cube_length // 2 + 1

    cube = []
    for x in range(cube_length):
        column = []
        for y in range(cube_length):
            layer = []
            for z in range(cube_length):
                layer.append(".")
            column.append(layer)
        cube.append(column)

    start_idx = (middle - 1) - len(value) // 2
    for r in range(len(value)):
        for c in range(len(value[0])):
            cube[middle - 1][start_idx + r][start_idx + c] = value[r][c]

    for _ in range(step):
        cube = next_step(cube)

    return sum(1 for r in cube for c in r for l in c if l == "#")


def part2():
    value = data.INPUT

    def get_neigbours(
        col, row, layer, doc, col_length, row_length, layer_length, doc_length
    ):
        neigbours = []

        for col_idx in range(col - 1, col + 2):
            for row_idx in range(row - 1, row + 2):
                for layer_idx in range(layer - 1, layer + 2):
                    for doc_idx in range(doc - 1, doc + 2):
                        if (
                            -1 in [col_idx, row_idx, layer_idx, doc_idx]
                            or col_idx == col_length
                            or row_idx == row_length
                            or layer_idx == layer_length
                            or doc_idx == doc_length
                        ):
                            continue

                        if (col, row, layer, doc) == (
                            col_idx,
                            row_idx,
                            layer_idx,
                            doc_idx,
                        ):
                            continue

                        neigbours.append((col_idx, row_idx, layer_idx, doc_idx))

        return neigbours

    def next_step(value):
        result = copy.deepcopy(value)

        for row_idx, row in enumerate(value):
            for col_idx, col in enumerate(row):
                for layer_idx, layer in enumerate(col):
                    for doc_idx, doc in enumerate(layer):
                        current = value[row_idx][col_idx][layer_idx][doc_idx]

                        neigbours = get_neigbours(
                            col_idx,
                            row_idx,
                            layer_idx,
                            doc_idx,
                            len(value[0]),
                            len(value),
                            len(value[0][0]),
                            len(value[0][0][0]),
                        )
                        lights_on = sum(
                            1 for n in neigbours if value[n[1]][n[0]][n[2]][n[3]] == "#"
                        )

                        if current == "#" and lights_on not in [2, 3]:
                            result[row_idx][col_idx][layer_idx][doc_idx] = "."
                            continue

                        if current == "." and lights_on == 3:
                            result[row_idx][col_idx][layer_idx][doc_idx] = "#"
                            continue

        return result

    step = 6
    cube_length = step * 2 + len(value) + 1
    middle = cube_length // 2 + 1

    cube = []
    for x in range(cube_length):
        column = []
        for y in range(cube_length):
            layer = []
            for z in range(cube_length):
                document = []
                for w in range(cube_length):
                    document.append(".")
                layer.append(document)
            column.append(layer)
        cube.append(column)

    start_idx = (middle - 1) - len(value) // 2
    for r in range(len(value)):
        for c in range(len(value[0])):
            cube[middle - 1][middle - 1][start_idx + r][start_idx + c] = value[r][c]

    for _ in range(step):
        cube = next_step(cube)

    return sum(1 for r in cube for c in r for l in c for d in l if d == "#")
