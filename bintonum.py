#My E. Lovell 2018-03-01 - binary to number, med hjälp av peter

import math
#binary = input("question")
def btn(binary):
    exponent = 0
    output = 0
    index = len(binary) -1

    while index >= 0:
        if binary[index] == "1":
            output += 2**exponent
            exponent += 1
            index -= 1
    return output

print (btn("1010"))
