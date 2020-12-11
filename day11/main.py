from copy import deepcopy

import day11.data as data


def part1():
    value = data.INPUT

    def get_neigbours(col, row, col_length, row_length):
        neigbours = []

        for col_idx in range(col - 1, col + 2):
            for row_idx in range(row - 1, row + 2):
                if (
                    -1 in [col_idx, row_idx]
                    or col_idx == col_length
                    or row_idx == row_length
                ):
                    continue

                if (col, row) == (col_idx, row_idx):
                    continue

                neigbours.append((col_idx, row_idx))

        return neigbours

    def next_step(value):
        result = deepcopy(value)

        for row_idx, row in enumerate(value):
            for col_idx, col in enumerate(row):
                current = value[row_idx][col_idx]
                if current == ".":
                    continue

                neigbours = get_neigbours(col_idx, row_idx, len(value[0]), len(value))
                occupied_seats = sum(1 for n in neigbours if value[n[1]][n[0]] == "#")

                if current == "L" and occupied_seats == 0:
                    result[row_idx][col_idx] = "#"
                    continue

                if current == "#" and occupied_seats > 3:
                    result[row_idx][col_idx] = "L"
                    continue

        return result

    next_value = next_step(value)

    while value != next_value:
        value = deepcopy(next_value)
        next_value = next_step(value)

    return sum(1 for r in value for c in r if c == "#")


def part2():
    value = data.INPUT

    def get_neigbours(col, row, col_length, row_length):
        neigbours = []
        seats = ["L", "#"]

        # Up
        for row_idx in range(row - 1, -1, -1):
            if value[row_idx][col] in seats:
                neigbours.append((col, row_idx))
                break

        # Down
        for row_idx in range(row + 1, row_length):
            if value[row_idx][col] in seats:
                neigbours.append((col, row_idx))
                break

        # Left
        for col_idx in range(col - 1, -1, -1):
            if value[row][col_idx] in seats:
                neigbours.append((col_idx, row))
                break

        # Right
        for col_idx in range(col + 1, col_length):
            if value[row][col_idx] in seats:
                neigbours.append((col_idx, row))
                break

        # Up-Left
        for step in range(1, max(col_length, row_length)):
            col_idx = col - step
            row_idx = row - step

            if not (col_idx > -1 and row_idx > -1):
                break

            if value[row_idx][col_idx] in seats:
                neigbours.append((col_idx, row_idx))
                break

        # Up-Right
        for step in range(1, max(col_length, row_length)):
            col_idx = col + step
            row_idx = row - step

            if not (col_idx < col_length and row_idx > -1):
                break

            if value[row_idx][col_idx] in seats:
                neigbours.append((col_idx, row_idx))
                break

        # Down-Left
        for step in range(1, max(col_length, row_length)):
            col_idx = col - step
            row_idx = row + step

            if not (col_idx > -1 and row_idx < row_length):
                break

            if value[row_idx][col_idx] in seats:
                neigbours.append((col_idx, row_idx))
                break

        # Down-Right
        for step in range(1, max(col_length, row_length)):
            col_idx = col + step
            row_idx = row + step

            if not (col_idx < col_length and row_idx < row_length):
                break

            if value[row_idx][col_idx] in seats:
                neigbours.append((col_idx, row_idx))
                break

        return neigbours

    def next_step(value):
        result = deepcopy(value)

        for row_idx, row in enumerate(value):
            for col_idx, col in enumerate(row):
                current = value[row_idx][col_idx]
                if current == ".":
                    continue

                neigbours = get_neigbours(col_idx, row_idx, len(value[0]), len(value))
                occupied_seats = sum(1 for n in neigbours if value[n[1]][n[0]] == "#")

                if current == "L" and occupied_seats == 0:
                    result[row_idx][col_idx] = "#"
                    continue

                if current == "#" and occupied_seats > 4:
                    result[row_idx][col_idx] = "L"
                    continue

        return result

    next_value = next_step(value)

    while value != next_value:
        value = deepcopy(next_value)
        next_value = next_step(value)

    return sum(1 for r in value for c in r if c == "#")
