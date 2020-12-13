from functools import reduce
from operator import mul

import day13.data as data


def part1():
    value = data.INPUT

    arrival_time = value[0]
    bus_services = [x for x in value[1] if isinstance(x, int)]

    result = 0
    min_wait = 99999999999999
    for bus_no in bus_services:
        wait_time = bus_no - (arrival_time % bus_no)

        if wait_time < min_wait:
            min_wait = wait_time
            result = wait_time * bus_no

    return result


def part2():
    value = data.INPUT[1]

    bus_services = [x for x in value if isinstance(x, int)]

    max_bus = max(bus_services)
    max_bus_idx = value.index(max_bus)

    # tam bolen
    aliquots = [x for x in bus_services if (value.index(x) - max_bus_idx) % x == 0]
    non_aliquots = [x for x in bus_services if x not in aliquots]

    step = reduce(mul, aliquots, 1)

    number = 0
    while True:
        result = True
        for bus in non_aliquots:
            result &= ((number - max_bus_idx) + value.index(bus)) % bus == 0

            if not result:
                break

        if result:
            return number - max_bus_idx

        number += step

    return None
