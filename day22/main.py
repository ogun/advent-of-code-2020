from copy import deepcopy

import day22.data as data


def part1():
    value = deepcopy(data.INPUT)

    p1 = value["Player 1"]
    p2 = value["Player 2"]

    while p1 and p2:
        p1_card = p1.pop()
        p2_card = p2.pop()

        if p1_card > p2_card:
            p1.insert(0, p1_card)
            p1.insert(0, p2_card)
        else:
            p2.insert(0, p2_card)
            p2.insert(0, p1_card)

    winner = p1 if p1 else p2
    return sum((idx + 1) * value for idx, value in enumerate(winner))


def part2():
    value = deepcopy(data.INPUT)

    p1 = value["Player 1"]
    p2 = value["Player 2"]

    def insert(arr, first, second, reverse):
        if reverse:
            arr.insert(0, second)
            arr.insert(0, first)
            return

        arr.insert(0, first)
        arr.insert(0, second)

    def get_winner(p1, p2):
        visited = []
        while p1 and p2:
            key = f"{p1}|{p2}"

            if key in visited:
                return 1

            visited.append(key)

            card1, card2 = p1.pop(), p2.pop()
            if len(p1) >= card1 and len(p2) >= card2:
                p1_new_deck = p1[-1 * card1 :]
                p2_new_deck = p2[-1 * card2 :]

                winner = get_winner(p1_new_deck, p2_new_deck)

                insert(p1 if winner == 1 else p2, card1, card2, winner == 2)
            else:
                insert(p1 if card1 > card2 else p2, card1, card2, card2 > card1)

        return 1 if p1 else 2

    get_winner(p1, p2)

    winner = p1 if p1 else p2
    return sum((idx + 1) * value for idx, value in enumerate(winner))
