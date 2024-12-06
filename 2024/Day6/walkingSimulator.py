import time

moveDirections = [
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
]
moveIndex = 0
emptySymbol = "."
barrierSymbol = "#"
guardSymbol = "^"

extraBarrierIndex = []
maybeLoopCount = 0 # How long have we been on repeat tiles
maxLoopCount = 0   # What is the largest loop our board could have

startingPosition = []
position = []
roomMap = []
size = []
visitedTiles = []

def reset():
    global roomMap, size, visitedTiles, moveIndex, position, startingPosition
    roomMap.clear()
    size.clear()
    visitedTiles.clear()
    startingPosition.clear()
    position.clear()
    moveIndex = 0

def parse(file):
    global position, startingPosition, maxLoopCount
    lineCount = 0
    for line in file:
        guard = line.find(guardSymbol)
        if guard != -1:
            startingPosition = [lineCount, guard]
            position = startingPosition.copy()
        lineCount += 1
        roomMap.append(line.strip("\n"))
    size.append(len(roomMap)) #X
    size.append(len(roomMap[0])) #Y
    maxLoopCount = (size[0] * 2) + (size[1] * 2) # perimeter

def solve_easy() -> int:
    visitedTiles.append([position[0], position[1]])
    while step(position[0], position[1]):
        pass
    return len(visitedTiles)

def solve_hard() -> int:
    global moveIndex, position, visitedTiles, roomMap, extraBarrierIndex
    total = 0
    for x in range(0, size[0]):
        for y in range(0, size[1]):
            if not point_empty(x, y):
                continue
            print("Trying position", x, ", ", y)
            extraBarrierIndex = [x, y]
            visitedTiles.append([position[0], position[1]])
            while step(position[0], position[1]):
                if is_stuck_in_loop():
                    print("Loop location: ", x, ", ", y)
                    total += 1
                    break
            position = startingPosition.copy()
            moveIndex = 0
            visitedTiles.clear()
    return total

def is_stuck_in_loop() -> bool:
    return maybeLoopCount >= maxLoopCount

def step(x, y) -> bool: # return if more work is needed
    global visitedTiles, maybeLoopCount, position
    x += moveDirections[moveIndex][0]
    y += moveDirections[moveIndex][1]
    while True:
        if not point_in_bounds(x, y):
            return False
        if point_blocked(x, y):
            x -= moveDirections[moveIndex][0]
            y -= moveDirections[moveIndex][1]
            turn()
            x += moveDirections[moveIndex][0]
            y += moveDirections[moveIndex][1]
        else:
            break
    if point_is_unique(x, y):
        visitedTiles.append([x, y])
        maybeLoopCount = 0
    else:
        maybeLoopCount += 1
    position[0] = x
    position[1] = y
    return True

def point_is_unique(x, y) -> bool:
    point = [x, y]
    return point not in visitedTiles

def point_blocked(x, y) -> bool:
    if x == extraBarrierIndex[0] and y == extraBarrierIndex[1]: 
        return True
    return roomMap[x][y] == barrierSymbol

def point_empty(x, y) -> bool:
    return roomMap[x][y] == emptySymbol

def point_in_bounds(x, y) -> bool:
    return x >= 0 and y >= 0 and x < size[0] and y < size[1]

def turn():
    global moveIndex
    moveIndex += 1
    if moveIndex == len(moveDirections):
        moveIndex = 0

### Test Infrastructure ###

# Toggle Advanced mode
runHardTests = True

# Inputs and their expected results
inputs = {
    "test0" : [41, 6],
    "test1" : [2, 1],
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