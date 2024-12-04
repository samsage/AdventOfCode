import string

data = []

def reset():
    data.clear()

def parse(file):
    for line in file:
        data.append(line.strip("\n").split(" "))

def solve_easy() -> int:
    total = 0
    for list in data:
        if is_list_safe(list):
            total += 1
    return total

def solve_hard() -> int:
    total = 0
    for list in data:
        if is_any_list_permutation_safe(list):
            total += 1
    return total

def is_any_list_permutation_safe(list: list) -> bool:
    if is_list_safe(list):
        return True
    for i in range(0, len(list)):
        sublist = list.copy()
        del sublist[i]
        if is_list_safe(sublist):
            return True
    return False

def is_list_safe(list) -> bool:
    increasing = None
    previous = None
    for numStr in list:
        num = int(numStr)
        if previous == None:
            previous = num
            continue
        direction = num - previous > 0
        dif = abs(num - previous)
        if increasing == None:
            increasing = direction
        if dif < 1 or dif > 3 or increasing != direction:
            return False
        previous = num
    return True
        

### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [2, 4],
    "testFinal" : [None, None],
}

# Main
def run_tests():
    for input in inputs:
        expectedValue = inputs[input][1] if runHardTests else inputs[input][0]
        print("Running ", input)
        reset()
        with open(input, encoding="utf-8") as file:
            parse(file)
            result = solve_hard() if runHardTests else solve_easy()
            if(expectedValue == None):
                print("Result: ", result)
            elif result == expectedValue:
                print("Sucess! Result of ", result, " matches expected value ", expectedValue)
            else:
                print("Fail! Result of ", result, " does not match expected value ", expectedValue)
        print("")

run_tests()