# My E. Lovell 2019-03-08

if __name__ == '__main__':

birthday_dictionary = {
        'Albert Einstein': '1879-03-14',
        'Benjamin Franklin': '1706-01-17',
        'Ada Lovelace': '1815-12-10',
        'Donald Trump': '1946-06-14',
        'Rowan Atkinson': '1955-01-06',
        'Jeja Simic': '2002-03-27',
        'Peter Alnås': '2002-12-18',
        'My E. Lovell': '2002-12-25'}

print ("This is the birthday dictionary. We know the birthad of:\n")
for name in birthday_dictionary
    print (name)

print ("Who's birthday do you want to look up?")
name = input()
if name in birthday_dictionary:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

#currently not working
