from operator import add, mul

import day18.data as data


def calculate(rpn):
    op = {"+": add, "*": mul}

    number = []
    for token in rpn:
        if isinstance(token, int):
            number.append(token)
            continue

        left = number.pop()
        right = number.pop()

        number.append(op[token](left, right))

    return number[0]


def part1():
    value = data.INPUT

    # https://en.wikipedia.org/wiki/Reverse_Polish_notation
    def to_rpn(expr):
        expr = expr.replace(" ", "")
        expr = list(expr)

        # https://en.wikipedia.org/wiki/Shunting-yard_algorithm
        output, operator = [], []

        for token in expr:
            if token.isdigit():
                output.append(int(token))
            elif token in "+*":
                while operator and operator[-1] != "(":
                    output.append(operator.pop())

                operator.append(token)
            elif token == "(":
                operator.append("(")
            elif token == ")":
                while operator and (cur_operator := operator.pop()) != "(":
                    output.append(cur_operator)

        while operator:
            output.append(operator.pop())

        return output

    return sum(calculate(to_rpn(expr)) for expr in value)


def part2():
    value = data.INPUT

    # https://en.wikipedia.org/wiki/Reverse_Polish_notation
    def to_rpn(expr):
        expr = expr.replace(" ", "")
        expr = list(expr)

        # https://en.wikipedia.org/wiki/Shunting-yard_algorithm
        output, operator = [], []

        operators = {
            "+": 2,
            "*": 1,
        }

        for token in expr:
            if token.isdigit():
                output.append(int(token))
            elif token in "+*":
                while (
                    operator
                    and operator[-1] != "("
                    and operators[operator[-1]] > operators[token]
                ):
                    output.append(operator.pop())

                operator.append(token)
            elif token == "(":
                operator.append("(")
            elif token == ")":
                while operator and (cur_operator := operator.pop()) != "(":
                    output.append(cur_operator)

        while operator:
            output.append(operator.pop())

        return output

    return sum(calculate(to_rpn(expr)) for expr in value)
