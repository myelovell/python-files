#My E. Lovell 2019-03-20, bubblesort

from random import randint

lista = []
y = int(input("how many numbers do you want?\n"))
for i in range(y):
    yy = int(input())
    lista.append(yy)

def bubblesort(lista):
    changes = 0
    while changes == 0:
        changes = 1
        for i in range(len(lista) -1):
            if lista[i] > lista[i + 1]:
                n = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = n
                changes = 0
    return lista

print(bubblesort(lista))
