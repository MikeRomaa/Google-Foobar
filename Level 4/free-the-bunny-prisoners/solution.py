# To be honest although I somewhat understand the concept, I didn't
# come up with this solution, the instructions were just too unclear for me...
from itertools import combinations

def solution(num_buns, num_required):
    buns = [[] for i in range(num_buns)]
    for num, combination in enumerate(combinations(buns, num_buns - num_required + 1)):
        for item in combination:
            item.append(num)
    return buns