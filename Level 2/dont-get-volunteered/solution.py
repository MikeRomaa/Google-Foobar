def solution(src, dest):

    srcPos = (src % 8, src // 8, 0)                                                                               # Calculating coordinate position of starting point.
    destPos = (dest % 8, dest // 8)                                                                               # Calculating coordinate position of destination point.
    
    if srcPos[:2] == destPos:
        return 0

    moves = [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    visitState = [[False for i in range(8)] for i in range(8)]
    queue = [srcPos]
    visitState[srcPos[1]][srcPos[0]] = True

    while queue:
        currPos = queue[0]
        queue.remove(currPos)

        for move in moves:                                                                                        # Iterates through all possible knight moves from current position.
            possPos = (currPos[0] + move[0], currPos[1] + move[1], currPos[2] + 1)
            if not (0 <= possPos[0] <= 7) or not (0 <= possPos[1] <= 7) or visitState[possPos[1]][possPos[0]]:    # Rejects positions that are out of the matrix or have been visited in shorter moves.
                continue
            elif possPos[:2] == destPos:                                                                          # Returns number of moves taken if the position matches the destination.
                return possPos[2]
            else:
                visitState[possPos[1]][possPos[0]] = True
                queue.append(possPos)