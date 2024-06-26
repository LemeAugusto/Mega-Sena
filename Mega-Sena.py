from random import randint
import os

lista_de_jogos = []

while True:
    os.system('cls')

    # Variável para adicionar ou não para a lista

    d = True

    # Realizar o sorteio

    n1 = randint(1, 60)
    n2 = randint(1, 60)
    n3 = randint(1, 60)
    n4 = randint(1, 60)
    n5 = randint(1, 60)
    n6 = randint(1, 60)
    
    sorteios = (n1, n2, n3, n4, n5, n6)

    # Filtro I: Filtros repetidos no sorteio

    if n1 == n2:
        d = False
    else:
        if n1 == n3:
            d = False
        else:
            if n1 == n4:
                d = False
            else:
                if n1 == n5:
                    d = False
                else:
                    if n1 == n6:
                        d = False
                    else:
                        if n2 == n3:
                            d = False
                        else:
                            if n2 == n4:
                                d = False
                            else:
                                if n2 == n5:
                                    d = False
                                else:
                                    if n2 == n6:
                                        d = False
                                    else:
                                        if n3 == n4:
                                                d = False
                                        else:
                                            if n3 == n5:
                                                d = False
                                            else:
                                                if n3 == n6:
                                                    d = False
                                                else:
                                                    if n4 == n5:
                                                        d = False
                                                    else:
                                                        if n4 == n6:
                                                            d = False
                                                        else:
                                                            if n5 == n6:
                                                                d = False
    if d == True:
        lista_de_jogos.append(sorteios)
    
    # Filtro II: Sorteios idênticos

    lista_de_jogos_tupla = set(lista_de_jogos)
    sorteios2 = list(lista_de_jogos_tupla)
    sorteios = sorteios2
    print(sorteios)

    # Finalizar o script automaticamente

    if len(sorteios) == 50063860:
        break
