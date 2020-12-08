import day05.data as data


def part1():
    value = data.INPUT

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


def part2():
    value = data.INPUT

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
