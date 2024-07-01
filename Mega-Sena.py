from random import randint
import os

num = []
while True:
    os.system('cls')
    lista = []

    for i in range(1, 7):    # Realizar o sorteio
        sorteio = randint(1, 61)
        lista.append(sorteio)
    
    a = lista     # Deletar jogos idênticos
    b = set(lista)
    if len(b) < len(a):
        del lista
        continue
    lista = tuple(lista)
    num.append(lista)
    
    num_tuplas = set(num)    # Deletar sorteios idênticos
    num2 = list(num_tuplas)
    num = num2
    print(num)

    if len(num) == 50063860:    # Finalizar o script automaticamente
        break
