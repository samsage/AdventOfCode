import time


def reset():
    pass

def parse(file):
    pass

def solve_easy() -> int:
    total = 0
    return total

def solve_hard() -> int:
    total = 0
    return total


### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = False

# Inputs and their expected results
inputs = {
    "test0" : [None, None],
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