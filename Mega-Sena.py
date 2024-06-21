from random import randint
import os

num = []

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
    n7 = randint(1, 60)
    
    numbers = (n1, n2, n3, n4, n5, n6, n7)

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
                        if n1 == n7:
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
                                            if n2 == n7:
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
                                                            if n3 == n7:
                                                                d = False
                                                            else:
                                                                if n4 == n5:
                                                                    d = False
                                                                else:
                                                                    if n4 == n6:
                                                                        d = False
                                                                    else:
                                                                        if n4 == n7:
                                                                            d = False
                                                                        else:
                                                                            if n5 == n6:
                                                                                d = False
                                                                            else:
                                                                                if n5 == n7:
                                                                                    d = False
                                                                                else:
                                                                                    if n6 == n7:
                                                                                        d = False

    if d == True:
        num.append(numbers)
    
    # Filtro II: Sorteios idênticos

    num_tuplas = set(num)
    num2 = list(num_tuplas)
    num = num2
    print(num)

    # Finalizar o script automaticamente

    if len(num) == 50063860:
        break