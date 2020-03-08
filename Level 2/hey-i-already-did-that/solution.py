def solution(n, b):
    sequence = [n]
    repeatLen = 0
    found = False

    while not found:
        n = [digit for digit in str(n)]          # Converting given integer into a list of characters to create sorted versions.
        n.sort()
        y = ''.join(n)
        n.reverse()
        x = ''.join(n)
        z = int(x, b) - int(y, b)                # Doing subtraction after converting to base 10.

        if b != 10:                              # Converting result back to given base to apply the algorithm again.
            newNumber = ''
            while z >= b:
                q, r = divmod(z, b)
                newNumber = str(r) + newNumber
                z = q
            newNumber = str(z) + newNumber
            z = int(newNumber)
        n = z

        for elem in sequence:                    # Linear search to find occurence of the number and calculate the difference in indices.
            if elem == n:
                found = True
                repeatLen = len(sequence) - sequence.index(elem)
                break
        sequence.append(n)

    return repeatLen