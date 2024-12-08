from time import process_time
from vector import obj as Vector2

data = {}
size = Vector2(x=0, y=0)

antiNodes = []

def reset():
    global data, antiNodes
    data.clear()
    antiNodes.clear()

def parse(file):
    global data, size
    map = []
    for line in file:
        map.append(line.strip("\n"))
    size = Vector2(x=len(map[0]), y=len(map))
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            char = map[y][x]
            if char_is_signal(char):
                if char not in data:
                    data[char] = []
                data[char].append(Vector2(x=x, y=y))

def char_is_signal(char) -> bool:
    upperCase = char >= 'A' and char <= 'Z'
    lowerCase = char >= 'a' and char <= 'z'
    num       = char >= '0' and char <= '9'
    return upperCase or lowerCase or num

def in_bounds(pos) -> bool:
    return pos.x >= 0 and pos.y >= 0 and pos.x < size.x and pos.y < size.y

def is_new(pos) -> bool:
    return pos not in antiNodes

def get_left_antinode(pos1, pos2):
    return pos1 + (pos1 - pos2)

def get_right_antinode(pos1, pos2):
    return pos2 + (pos2 - pos1)

def get_all_antinodes(pos1, pos2):
    result = []
    dir = pos1 - pos2
    start1 = pos1
    start2 = pos2
    while in_bounds(pos1):
        result.append(pos1)
        pos1 = pos1 + dir
    while in_bounds(pos2):
        result.append(pos2)
        pos2 = pos2 - dir
    return result

def solve_easy() -> int:
    global antiNodes
    for symbol in data:
        for firstIndex in range(0, len(data[symbol])):
            for secondIndex in range(firstIndex + 1, len(data[symbol])):
                left = get_left_antinode(data[symbol][firstIndex], data[symbol][secondIndex])
                right = get_right_antinode(data[symbol][firstIndex], data[symbol][secondIndex])
                if in_bounds(left) and is_new(left):
                    antiNodes.append(left)
                if in_bounds(right) and is_new(right):
                    antiNodes.append(right)
    return len(antiNodes)

def solve_hard() -> int:
    global antiNodes
    for symbol in data:
        for firstIndex in range(0, len(data[symbol])):
            for secondIndex in range(firstIndex + 1, len(data[symbol])):
                nodes = get_all_antinodes(data[symbol][firstIndex], data[symbol][secondIndex])
                for node in nodes:
                    if is_new(node):
                        antiNodes.append(node)
    return len(antiNodes)


### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [14, 34],
    "test1" : [2, 5],
    "testFinal" : [None, None],
}

# Main
def run_tests():
    for input in inputs:
        expectedValue = inputs[input][1] if runHardTests else inputs[input][0]
        testStart = process_time()
        print("Running ", input)
        reset()
        with open(input, encoding="utf-8") as file:
            parse(file)
            result = solve_hard() if runHardTests else solve_easy()
            testTime = process_time() - testStart
            print("Test executed in ", testTime, " seconds")
            if(expectedValue == None):
                print("Result: ", result)
            elif result == expectedValue:
                print("Sucess! Result of ", result, " matches expected value ", expectedValue)
            else:
                print("Fail! Result of ", result, " does not match expected value ", expectedValue)
        print("")

run_tests()