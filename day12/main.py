from operator import add

import day12.data as data


def part1():
    value = data.INPUT

    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    direction_map = {
        "E": 0,
        "S": 1,
        "W": 2,
        "N": 3,
    }

    def change_direction(direction, instruction, units):
        motion = 1 if instruction == "R" else -1

        idx = directions.index(direction)
        idx = (idx + (motion * (units // 90))) % len(directions)

        return directions[idx]

    def move(location, direction, instruction, units):
        current_direction = direction

        if instruction in direction_map:
            current_direction = directions[direction_map[instruction]]

        return list(
            map(
                add,
                location,
                [units * current_direction[0], units * current_direction[1]],
            )
        )

    direction = directions[0]
    location = [0, 0]
    for step in value:
        instruction = step[0]
        units = step[1]

        if instruction in ["L", "R"]:
            direction = change_direction(direction, instruction, units)
        else:
            location = move(location, direction, instruction, units)

    return abs(location[0]) + abs(location[1])


def part2():
    value = data.INPUT

    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]

    direction_map = {
        "E": 0,
        "S": 1,
        "W": 2,
        "N": 3,
    }

    def change_waypoint(waypoint, instruction, units):
        if instruction in ["E", "S", "W", "N"]:
            current_direction = directions[direction_map[instruction]]
            return list(
                map(
                    add,
                    waypoint,
                    [units * current_direction[0], units * current_direction[1]],
                )
            )

        count = units // 90

        if (count % 2) == 1:
            waypoint = [waypoint[1], waypoint[0]]

        c = count % 4
        if instruction == "L":
            if c == 1:
                waypoint = [waypoint[0], -1 * waypoint[1]]
            elif c == 2:
                waypoint = [-1 * waypoint[0], -1 * waypoint[1]]
            else:
                waypoint = [-1 * waypoint[0], waypoint[1]]
        else:
            if c == 1:
                waypoint = [-1 * waypoint[0], waypoint[1]]
            elif c == 2:
                waypoint = [-1 * waypoint[0], -1 * waypoint[1]]
            else:
                waypoint = [waypoint[0], -1 * waypoint[1]]

        return waypoint

    def move(location, waypoint, instruction, units):
        return list(map(add, location, [units * waypoint[0], units * waypoint[1]]))

    waypoint = [10, -1]
    location = [0, 0]
    for step in value:
        instruction = step[0]
        units = step[1]

        if instruction == "F":
            location = move(location, waypoint, instruction, units)
        else:
            waypoint = change_waypoint(waypoint, instruction, units)

    return abs(location[0]) + abs(location[1])
