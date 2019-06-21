#My E. Lovell 2019-03-02, rövarspråket

words = input("meningen du vill översätta är:\n")
def translate(words):
    output = ("")
    konsonanter = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z" , "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z" ]
    for letters in  words:
        if letters in konsonanter:
            output += str(letters + "o" + letters)
        else:
            output += letters
    return output

print (translate(words))
