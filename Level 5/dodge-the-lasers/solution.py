import math

sqrt2m1 = 4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727
ten100 = 10**100

def s(n):
    sum = 0

    if n > 0:
        n100 = n * ten100
        nprime = ((n * sqrt2m1) / ten100)
        nprime100 = nprime * ten100
        sum_iter = (n * nprime100) + ((n * (n100 + ten100)) / 2) - ((nprime * (nprime100 + ten100)) / 2)
        sum += sum_iter - s(nprime)
    
    return sum

def solution(n):
    return str(s(int(n)) / ten100)