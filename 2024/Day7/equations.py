import time

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))

operators = [add, multiply]

equations = []

def reset():
    global equations
    equations.clear()

def parse(file):
    for line in file:
        halves = line.strip("\n").split(":")
        equation = [int(halves[0])]
        values = halves[1].strip(" ").split(" ")
        for value in values:
            equation.append(int(value))
        equations.append(equation)

def solve_easy() -> int:
    total = 0
    for equation in equations:
        print("Testing equation: ", equation)
        if is_equation_solvable(equation):
            total += equation[0]
    return total

def is_equation_solvable(equation: list) -> bool:
    goal = equation[0]
    result = equation[1]
    return try_operators(goal, result, equation, 2)

def try_operators(goal, result, equation, index) -> bool:
    if index == len(equation):
        return result == goal
    for op in operators:
        newResult = op(result, equation[index])
        if try_operators(goal, newResult, equation, index + 1):
            return True
    return False

def solve_hard() -> int:
    operators.append(concat)
    return solve_easy()


### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [3749, 11387],
    "testFinal" : [None, None],
}

# Main
def run_tests():
    for input in inputs:
        expectedValue = inputs[input][1] if runHardTests else inputs[input][0]
        testStart = time.process_time()
        print("Running ", input)
        reset()
        with open(input, encoding="utf-8") as file:
            parse(file)
            result = solve_hard() if runHardTests else solve_easy()
            testTime = time.process_time() - testStart
            print("Test executed in ", testTime, " seconds")
            if(expectedValue == None):
                print("Result: ", result)
            elif result == expectedValue:
                print("Sucess! Result of ", result, " matches expected value ", expectedValue)
            else:
                print("Fail! Result of ", result, " does not match expected value ", expectedValue)
        print("")

run_tests()