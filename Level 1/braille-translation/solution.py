def solution(s):
    # ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']   Add a (3) to above character
    # ['U', 'V', 'X', 'Y', 'Z',                     'W']   Add a (6) to above character (Except W which adds to J)
    firstRow = {
        'A': '100000',
        'B': '110000',
        'C': '100100',
        'D': '100110',
        'E': '100010',
        'F': '110100',
        'G': '110110',
        'H': '110010',
        'I': '010100',
        'J': '010110'
    }
    output = ''
    for letter in s:
        if letter.isupper():         # Adds uppercase modifier if character is uppercase.
            output += '000001'
        else:                        # Makes the character uppercase for further processing.
            letter = letter.upper()

        letterASCII = ord(letter)

        if letterASCII == 32:                                    # Character is a space
            output += '000000'
        elif letterASCII < 75:                                   # First row character
            output += firstRow[letter]
        elif letterASCII < 85:                                   # Second row character
            firstRowMap = firstRow[chr(letterASCII - 10)]        # firstRowMap finds the character "above" the current character
            output += firstRowMap[:2] + '1' + firstRowMap[-3:]   # Replaces third or sixth character with 1 based on position in "matrix"
        elif letterASCII < 87:                                   # Third row character before W
            firstRowMap = firstRow[chr(letterASCII - 20)]
            output += firstRowMap[:2] + '1' + firstRowMap[-3:-1] + '1'
        elif letterASCII == 87:                                  # Character is W
            firstRowMap = firstRow[chr(letterASCII - 13)]
            output += firstRowMap[:-1] + '1'
        elif letterASCII > 87:                                   # Third row character after W
            firstRowMap = firstRow[chr(letterASCII - 21)]
            output += firstRowMap[:2] + '1' + firstRowMap[-3:-1] + '1'

    return output