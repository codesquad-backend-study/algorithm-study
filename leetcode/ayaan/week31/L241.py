def diffWaysToCompute(expression):
    def compute(left, right, op):
        results = []
        for l in left:
            for r in right:
                results.append(eval(str(l) + op + str(r)))
        return results

    if expression.isdigit():
        return [int(input())]

    results = []
    for index, value in enumerate(expression):
        if value in "-+*":
            left = diffWaysToCompute(expression[:index])
            right = diffWaysToCompute(expression[index + 1:])

            results.extend(compute(left, right, value))
    return results

diffWaysToCompute("2*3-4*5")
