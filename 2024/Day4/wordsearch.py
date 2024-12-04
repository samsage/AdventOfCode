import string

searchText = "XMAS"
searchDirections = [
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
    [-1, 0],
    [-1, 1]
]

searchTextHard = "SAM" #heehee its me
searchDirectionsHard = [
    [ [1, 1], [-1, -1] ],
    [ [1, -1], [-1, 1] ]
]

lowerBound = [0, 0]
upperBound = [0, 0]
data = []


def reset():
    global data, upperBound
    data.clear()
    upperBound = [0, 0]

def parse(file):
    lineCount = 0
    for line in file:
        data.append(line.strip("\n"))
        upperBound[1] = len(data[-1])
        lineCount += 1
    upperBound[0] = lineCount

def solve_easy() -> int:
    total = 0
    for y in range(0, upperBound[1]):
        for x in range(0, upperBound[0]):
            if data[x][y] == searchText[0]:
                total += check_index(x, y)
    return total

def solve_hard() -> int:
    total = 0
    for y in range(0, upperBound[1]):
        for x in range(0, upperBound[0]):
            if data[x][y] == searchTextHard[1]:
                total += check_index_hard(x, y)
    return total

def check_index(x, y) -> int:
    count = 0
    for dir in searchDirections:
        searchIndex = 0
        posX = x
        posY = y
        while index_in_bounds(posX, posY) and searchIndex < len(searchText) and data[posX][posY] == searchText[searchIndex]:
            posX += dir[0]
            posY += dir[1]
            searchIndex += 1
            if searchIndex >= len(searchText):
                #print("Success at index (", x, ", ", y, ") in direction ", dir)
                count += 1
    return count

def check_index_hard(x, y) -> int:
    corner1 = get_letter_hard(x, y, searchDirectionsHard[0][0])
    corner3 = get_letter_hard(x, y, searchDirectionsHard[0][1])
    corner2 = get_letter_hard(x, y, searchDirectionsHard[1][0])
    corner4 = get_letter_hard(x, y, searchDirectionsHard[1][1])
    check1 = letter_matches_any_hard(corner1) and letter_matches_any_hard(corner3) and corner1 != corner3
    check2 = letter_matches_any_hard(corner2) and letter_matches_any_hard(corner4) and corner2 != corner4
    if check1 and check2:
        return 1
    return 0

def get_letter_hard(x, y, dir):
    x += dir[0]
    y += dir[1]
    if not index_in_bounds(x, y):
        return None
    return data[x][y]

def letter_matches_any_hard(letter) -> bool:
    return letter == searchTextHard[0] or letter == searchTextHard[2]

def index_in_bounds(x, y) -> bool:
    return x >= lowerBound[0] and y >= lowerBound[1] and x < upperBound[0] and y < upperBound[1]

### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [18, 9],
    "test1" : [6, 2],
    "test2" : [6, 2],
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