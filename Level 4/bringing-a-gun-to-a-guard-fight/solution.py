import math

def getMirrors(position, distance, dimensions):
    coords = []
    originX, originY = position
    xCoords, yCoords = [originX], [originY]
    expandX, expandY = int(math.ceil(distance / dimensions[0])), int(math.ceil(distance / dimensions[1]))     # Calculate amount to expand grid by in positive X and Y directions

    for x in range(1, expandX + 2):                                                                           # Get all possible X coordinates
        originX = -originX + 2 * (dimensions[0] * x)
        xCoords += [originX]
    for y in range(1, expandY + 2):                                                                           # Get all possible Y coordinates
        originY = -originY + 2 * (dimensions[1] * y)
        yCoords += [originY]
    for x in xCoords:                                                                                         # Generate intersections of the positions for all four quadrants
        for y in yCoords:
            coords += [[x,y], [-x,y], [x,-y], [-x,-y]]
            
    return coords

def solution(dimensions, your_position, guard_position, distance):
    playerPositions = getMirrors(your_position, distance, dimensions)                                         # Generate list of mirrored player positions
    guardPositions = getMirrors(guard_position, distance, dimensions)                                         # Generate list of mirrored guard positions

    counter = 0
    vectors = {}

    for position in playerPositions:                                                                          # Get unique angle and distance to other player positions and add them to dict
        deltaPos = position[0] - your_position[0],position[1] - your_position[1]
        vectorDist, vectorAngle = math.hypot(*deltaPos), math.atan2(*deltaPos)
        if vectorDist <= distance and vectorAngle not in vectors:
            vectors[vectorAngle] = vectorDist

    for position in guardPositions:                                                                           # Get unique angle and ditance to other guard positions
        deltaPos = position[0] - your_position[0], position[1] - your_position[1]
        vectorDist, vectorAngle = math.hypot(*deltaPos), math.atan2(*deltaPos)
        if vectorDist <= distance and (vectorAngle not in vectors or vectorDist <= vectors[vectorAngle]):     # Check if the vector intersects with another coordinate
            vectors[vectorAngle] = vectorDist
            counter += 1

    return counter