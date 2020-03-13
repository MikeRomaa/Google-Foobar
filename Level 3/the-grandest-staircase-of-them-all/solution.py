def solution(n):
    # Generating function for partitions with distinct parts:
    # P_d(n) = prod((1 + x)(1 + x^2)...(1 + x^n))
    coeffs = [1] + [0] * n                           # Creates list of 1 and 0 * x^i, where 1 <= i <= n.

    for power in range(1, n + 1):
        for term in range(n, power - 1, -1):         # Iterating through all of the terms up to x^n in reverse.
            coeffs[term] += coeffs[term - power]     # Doing polynomial multiplication with only the coefficients.
    return coeffs[n] - 1                             # Number of partitions with distinct parts ignoring n + 0.