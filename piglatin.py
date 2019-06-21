# My E. Lovell 2019-03-13, piglatin codeacademy

print ("Welcome to the Pig Latin Translator")

# pyg = 'ay'
# original = input('Enter a word:')
#
# if len(original) > 0 and original.isalpha():
#   word = original.lower()
#   first = word[0]
#   new_word = word + first + pyg
#   new_word = new_word[1:len(new_word)]
#   print (new_word)
# else:
#     print ("empty")



    original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    original= original.lower()
    original = original + original[0] + 'ay'
    original[0] = ''
    print (original)
else:
    print ('empty')
