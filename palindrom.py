#  My E. Lovell 2019-03-07, palindrom

def palindrom(word):
    drow = word[::-1]

    if (word == drow):
        print ("the word is already a palindrome")

    else:
        print ("your word is not a palindrome")

word = input("write your word please:\n")

palindrom(word)
