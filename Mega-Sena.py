from random import randint
import os

jogos = []
while True:
    os.system('cls')
    lista = []

    for i in range(1, 7):    # Realizar o sorteio
        sorteio = randint(1, 61)
        lista.append(sorteio)
    
    if len(lista) != len(set(lista)):    # Deletar sorteios idêntico
        del lista
        continue
    lista = tuple(lista)    # Conversão necessária
    jogos.append(lista)
    
    jogos_tuplas = set(jogos)    # Deletar jogos idênticos
    jogos_clone = list(jogos_tuplas)
    jogos = jogos_clone
    print(jogos)

    if len(jogos) == 50063860:    # Finalizar automaticamente
        break
