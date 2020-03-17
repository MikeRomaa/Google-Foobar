import time
import operator

def solution(start, length):
    checksum = 0

    for row, firstID in enumerate(xrange(start, start + length ** 2, length)):               # Creates enumerated "rows" with all of the numbers.
        checksum ^= reduce(operator.xor, xrange(firstID, firstID + length - row))            # Cumulitavely XORs the "rows" using reduce, ignoring the necessary digits at the end.
    
    return checksum


start_time = time.time()
print(solution(0,10000))
print("--- %s seconds ---" % (time.time() - start_time))