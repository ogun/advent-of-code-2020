from copy import deepcopy
from functools import reduce
from operator import mul

import re
import day20.data as data


def flip(original):
    return list(zip(*original))


def rotate(original):
    return list(zip(*original[::-1]))


def get_corners(tile):
    return [tile[0], [c[-1] for c in tile], tile[-1], [c[0] for c in tile]]


def get_unique_corners(value):
    just_corners = {}
    for key in value:
        tile = value[key]
        just_corners[key] = get_corners(tile)

    all_corners = [arr for cor in just_corners.values() for arr in cor]
    unique_corners = [
        cor
        for cor in all_corners
        if all_corners.count(cor) + all_corners.count(list(reversed(cor))) == 1
    ]

    return just_corners, unique_corners


def part1():
    value = data.INPUT

    just_corners, unique_corners = get_unique_corners(value)

    tile_corners = []
    for key in just_corners:
        tile = just_corners[key]

        if sum(1 for c in tile if c in unique_corners) == 2:
            tile_corners.append(key)

    return reduce(mul, tile_corners, 1)


def get_picture_information(value):
    value = deepcopy(value)

    border_count = 12
    picture_information = {}
    for _ in range(6):
        just_corners, unique_corners = get_unique_corners(value)

        picture_information[border_count] = {"c": {}, "e": {}, "a": []}
        for key in just_corners:
            tile = just_corners[key]

            tile_unique_corner = [c for c in tile if c in unique_corners]
            sum_unique_corner = len(tile_unique_corner)
            if sum_unique_corner == 1:
                picture_information[border_count]["e"][key] = tile_unique_corner
                picture_information[border_count]["a"].append(key)
            elif sum_unique_corner == 2:
                picture_information[border_count]["c"][key] = tile_unique_corner
                picture_information[border_count]["a"].append(key)

        for border in list(picture_information[border_count]["e"].keys()) + list(
            picture_information[border_count]["c"].keys()
        ):
            del value[border]

        border_count -= 2

    return picture_information


def find_match(grid, neighbour_idx, all_set, value, left, right, top, bottom):

    while not grid[neighbour_idx[1]][neighbour_idx[0]]:
        for key in all_set:
            if key not in value:
                continue

            next_tile = value.pop(key)
            result, result_tile = control_edges(left, right, top, bottom, next_tile)

            if result:
                return {key: result_tile}
            else:
                value[key] = next_tile


def part2():
    value = data.INPUT

    picture_information = get_picture_information(value)

    first_four = picture_information[12]
    first_four_tiles = list(first_four["c"].keys())
    first_id = first_four_tiles[3]

    grid = [[None for r in range(12)] for c in range(12)]

    grid[11][0] = {first_id: value[first_id]}
    del value[first_id]
    picture_information[12]["a"].remove(first_id)

    for xx in range(6):
        dxx = 2 * xx

        item_count = 12 - dxx
        max_idx = 11 - xx
        min_idx = 0 + xx

        all_set = picture_information[item_count]["a"]

        for i in range(min_idx, max_idx + 1):
            neighbour_idx = (i, max_idx)

            if grid[neighbour_idx[1]][neighbour_idx[0]]:
                continue

            left, right, top, bottom = get_neighbours(grid, neighbour_idx)
            grid[neighbour_idx[1]][neighbour_idx[0]] = find_match(
                grid, neighbour_idx, all_set, value, left, right, top, bottom
            )

        for i in range(max_idx, min_idx - 1, -1):
            neighbour_idx = (max_idx, i)

            if grid[neighbour_idx[1]][neighbour_idx[0]]:
                continue

            left, right, top, bottom = get_neighbours(grid, neighbour_idx)
            grid[neighbour_idx[1]][neighbour_idx[0]] = find_match(
                grid, neighbour_idx, all_set, value, left, right, top, bottom
            )

        for i in range(max_idx, min_idx - 1, -1):
            neighbour_idx = (i, min_idx)

            if grid[neighbour_idx[1]][neighbour_idx[0]]:
                continue

            left, right, top, bottom = get_neighbours(grid, neighbour_idx)
            grid[neighbour_idx[1]][neighbour_idx[0]] = find_match(
                grid, neighbour_idx, all_set, value, left, right, top, bottom
            )

        for i in range(min_idx, max_idx + 1):
            neighbour_idx = (min_idx, i)

            if grid[neighbour_idx[1]][neighbour_idx[0]]:
                continue

            left, right, top, bottom = get_neighbours(grid, neighbour_idx)
            grid[neighbour_idx[1]][neighbour_idx[0]] = find_match(
                grid, neighbour_idx, all_set, value, left, right, top, bottom
            )

    picture = grid_to_picture(grid)
    for _ in range(2):
        for _ in range(4):
            one_line = "".join(picture)
            dragon = r"(?=#.{77}#.{4}##.{4}##.{4}###.{77}#.{2}#.{2}#.{2}#.{2}#.{2}#)"
            match_count = len(re.findall(dragon, one_line))
            if match_count != 0:
                return one_line.count("#") - match_count * dragon.count("#")

            picture = deepcopy(["".join(x) for x in rotate(picture)])
        picture = deepcopy(["".join(x) for x in flip(picture)])

    return None


def grid_to_picture(grid):
    picture = [[None for r in range(96)] for c in range(96)]

    for row in range(12):
        for col in range(12):
            inner_grid = list(grid[row][col].values())[0]
            row_idx = 0
            for y in range(10):
                if y % 10 in [0, 9]:
                    continue

                col_idx = 0
                for x in range(10):
                    if x % 10 in [0, 9]:
                        continue
                    r = 8 * row + row_idx
                    c = 8 * col + col_idx
                    picture[r][c] = inner_grid[y][x]

                    col_idx += 1
                row_idx += 1

    new_picture = []
    for i in range(96):
        new_picture.append("".join(picture[i]))

    return new_picture


def get_neighbours(grid, current_pos):
    r = list(range(12))

    left = None
    if current_pos[0] - 1 in r and current_pos[1] in r:
        left = grid[current_pos[1]][current_pos[0] - 1]

    right = None
    if current_pos[0] + 1 in r and current_pos[1] in r:
        right = grid[current_pos[1]][current_pos[0] + 1]

    top = None
    if current_pos[1] - 1 in r and current_pos[0] in r:
        top = grid[current_pos[1] - 1][current_pos[0]]

    bottom = None
    if current_pos[1] + 1 in r and current_pos[0] in r:
        bottom = grid[current_pos[1] + 1][current_pos[0]]

    left_val = list(left.values())[0] if left else None
    right_val = list(right.values())[0] if right else None
    top_val = list(top.values())[0] if top else None
    bottom_val = list(bottom.values())[0] if bottom else None
    return left_val, right_val, top_val, bottom_val


def get_neighbours_idx(grid, current_pos):
    left = (current_pos[0], current_pos[1] - 1)
    right = (current_pos[0], current_pos[1] + 1)
    top = (current_pos[0] - 1, current_pos[1])
    bottom = (current_pos[0] + 1, current_pos[1])
    return left, right, top, bottom


def get_left(arr):
    return [c[0] for c in arr]


def get_top(arr):
    return list(arr[0])


def get_right(arr):
    return [c[-1] for c in arr]


def get_bottom(arr):
    return list(arr[-1])


def control_edges(left_tile, right_tile, top_tile, bottom_tile, next_tile):
    right_border = get_right(left_tile) if left_tile else None
    left_border = get_left(right_tile) if right_tile else None
    bottom_border = get_bottom(top_tile) if top_tile else None
    top_border = get_top(bottom_tile) if bottom_tile else None

    fit = True
    for _ in range(2):
        for _ in range(4):
            n_right_border = get_right(next_tile)
            n_left_border = get_left(next_tile)
            n_top_border = get_top(next_tile)
            n_bottom_border = get_bottom(next_tile)

            left, right, top, bottom = False, False, False, False
            fit = True

            if right_border:
                if n_left_border != right_border:
                    fit = False
                    next_tile = rotate(next_tile)
                    continue
                left = True

            if left_border:
                if n_right_border != left_border:
                    fit = False
                    next_tile = rotate(next_tile)
                    continue
                right = True

            if bottom_border:
                if n_top_border != bottom_border:
                    fit = False
                    next_tile = rotate(next_tile)
                    continue
                top = True

            if top_border:
                if n_bottom_border != top_border:
                    fit = False
                    next_tile = rotate(next_tile)
                    continue
                bottom = True

            break

        if fit:
            break

        next_tile = flip(next_tile)

    if fit:
        return True, next_tile

    return False, next_tile
