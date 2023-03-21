hexNumbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None

    if len(hexNum) == 1:
        decNum = hexNumbers[hexNum]
        print(decNum)

    else:
        decNum2 = 0
        counter = 0
        result = 0
        lengthHex = len(hexNum)
        counterFor16 = lengthHex
        while counterFor16 >= 1:
            counterFor16 = counterFor16 - 1
            decNum2 = (hexNumbers[hexNum[counter]] * (16 ** counterFor16))
            result = result + decNum2
            counter = counter + 1
        print(result)
    pass

hexToDec('A')
hexToDec('0')
hexToDec('1B')
hexToDec('3C0')
hexToDec('A6G')
hexToDec('ZZTOP')