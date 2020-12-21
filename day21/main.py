from functools import reduce

import day21.data as data


def part1():
    value = data.INPUT

    allergens = {}
    for allergens_ingredients in value:
        allergen_list = allergens_ingredients[0]
        ingredient_list = set(allergens_ingredients[1].split())

        for allergen in allergen_list:
            if allergen not in allergens:
                allergens[allergen] = []

            allergens[allergen].append(ingredient_list)

    possible_allergenic_ingredients = set()
    for allergen in allergens:
        ingredients = reduce(
            set.intersection, allergens[allergen][1:], allergens[allergen][0]
        )
        possible_allergenic_ingredients.update(ingredients)

    all_ingredients = {x for l in allergens.values() for i in l for x in i}
    non_allergenic_ingredients = all_ingredients - possible_allergenic_ingredients

    return sum(
        1 for a_i in value for i in a_i[1].split() if i in non_allergenic_ingredients
    )


def part2():
    value = data.INPUT

    allergens = {}
    for allergens_ingredients in value:
        allergen_list = allergens_ingredients[0]
        ingredient_list = set(allergens_ingredients[1].split())

        for allergen in allergen_list:
            if allergen not in allergens:
                allergens[allergen] = []

            allergens[allergen].append(ingredient_list)

    possible_allergenic_ingredients = {}
    for allergen in allergens:
        ingredients = reduce(
            set.intersection, allergens[allergen][1:], allergens[allergen][0]
        )
        possible_allergenic_ingredients[allergen] = ingredients

    while any(len(x) > 1 for x in possible_allergenic_ingredients.values()):
        unique = [
            list(x)[0] for x in possible_allergenic_ingredients.values() if len(x) == 1
        ]

        for key in possible_allergenic_ingredients:
            allergenic_list = possible_allergenic_ingredients[key]
            if len(allergenic_list) == 1:
                continue

            for u in unique:
                if u in allergenic_list:
                    allergenic_list.remove(u)

    result = []
    for key in sorted(possible_allergenic_ingredients):
        element_set = possible_allergenic_ingredients[key]
        if element_set:
            result.append(element_set.pop())

    return ",".join(result)
