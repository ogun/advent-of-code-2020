import day07.data as data


def part1():
    value = data.INPUT

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


def part2():
    value = data.INPUT

    def bag_count(bags):
        total_bag = 0

        for bag in bags:
            total_bag += bag[0] + bag[0] * bag_count(value[bag[1]])

        return total_bag

    return bag_count(value["shiny gold"])
