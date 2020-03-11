def solution(x,y):
    x = int(x)
    y = int(y)
    generations = 0

    if (x % 2 == 0 and y % 2 == 0) or x < 1 or y < 1:
        return 'impossible'

    while (x > 1 or y > 1):
        if x == 1 or y == 1:                    # If one of the numbers is one, their difference is the reminaing number of generations needed.
            generations += abs(x - y)
            break
        elif x == 0 or y == 0:                  # If either number goes below zero, then the combination is impossible.
            return 'impossible'
        elif x > y:
            generations += x // y
            x %= y
        else:
            generations += y // x
            y %= x
    
    return str(generations)

print(solution(17,16))