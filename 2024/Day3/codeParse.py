import re

mulPattern = re.compile(r"mul\([0-9]{1,3},[0-9]{1,3}\)")
offPattern = re.compile(r"don't\(\)")
onPattern = re.compile(r"do\(\)")

data = ""
offIndex = None
onIndex = 0

def reset():
    global data, offIndex, onIndex
    data = ""
    offIndex = None
    onIndex = 0

def parse(file):
    global data
    for line in file:
        data += line.strip("\n")

def solve_easy() -> int:
    total = 0
    matches = mulPattern.findall(data)
    for match in matches:
        total += multiply(match)
    return total

def solve_hard() -> int:
    total = 0
    mulIter = mulPattern.finditer(data)
    onIter = onPattern.finditer(data)
    offIter = offPattern.finditer(data)
    set_next_disabled_range(offIter, onIter)
    for match in mulIter:
        start = match.span()[0]
        if start < offIndex:
            total += multiply(match.group())
        elif start > onIndex:
            total += multiply(match.group())
            set_next_disabled_range(offIter, onIter)
    return total

def set_next_disabled_range(offIter, onIter):
    global offIndex
    global onIndex
    while offIndex == None or offIndex < onIndex:
        match = next(offIter, None)
        offIndex = match.span()[0] if match != None else 10000000 # Very big int
    while onIndex == None or offIndex > onIndex:
        match = next(onIter, None)
        onIndex = match.span()[0] if match != None else 10000001 # Very big int + 1
    print("Disabling range ", offIndex, " to ", onIndex)

def multiply(str) -> int:
    params = str.split('(')[1].split(')')[0].split(',')
    return int(params[0]) * int(params[1])

### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [161, 48],
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