
listOne = []
listTwo = []

def reset():
    listOne.clear()
    listTwo.clear()

def parse(file):
    for line in file:
        values = line.strip("\n").split(" ")
        listOne.append(int(values[0]))
        listTwo.append(int(values[-1]))

def solve_easy() -> int:
    total = 0
    listOne.sort()
    listTwo.sort()
    for i in range(0, len(listOne)):
        total += abs(listOne[i] - listTwo[i])
    return total

def solve_hard() -> int:
    total = 0
    for num in listOne:
        total += num * listTwo.count(num)
    return total

# Inputs and their expected results
runHardTests = True
inputs = {
    "test0" : [11, 31],
    "testFinal" : [None, None],
}

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