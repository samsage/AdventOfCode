import time
from functools import cmp_to_key

rules = []
pageOrders = []

def reset():
    global rules, pageOrders
    rules.clear()
    pageOrders.clear()

def parse(file):
    rulesDone = False
    for line in file:
        if line == "\n":
            rulesDone = True
            continue
        if rulesDone:
            pageOrders.append( list(map(int, line.strip("\n").split(","))) )
        else:
            rules.append( list(map(int, line.strip("\n").split("|"))) )

def solve_easy() -> int:
    total = 0
    for pageList in pageOrders:
        if order_valid(pageList):
            total += get_middle_value(pageList)
    return total

def solve_hard() -> int:
    total = 0
    for pageList in pageOrders:
        if order_valid(pageList):
            continue
        else:
            newList = fix_order(pageList)
            total += get_middle_value(newList)
    return total

def fix_order(pageList: list) -> list:
    return sorted(pageList, key=cmp_to_key(compare))

def compare(element1, element2) -> bool:
    for rule in rules:
        if rule[0] == element1 and rule[1] == element2:
            return -1
        elif rule[1] == element1 and rule[0] == element2:
            return 1
    return 0

def order_valid(pageList) -> bool:
    for index in range(1, len(pageList)):
        num = pageList[index]
        for rule in rules:
            if rule[0] == num:
                for previousIndex in range(0, index):
                    if(pageList[previousIndex] == rule[1]): # Before but should have been after
                        return False
    return True
                

def get_middle_value(pageList) -> int:
    index = int(len(pageList) / 2)
    return pageList[index]

### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [143, 123],
    "test1" : [0, 6],
    "testFinal" : [None, None],
}

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

# Main
run_tests()