import random
import time

Lista = []

#BubbleSort
def BubbleSort(Lista):
    ordenado = False

    while ordenado == False:
        ordenado = True
        for i in range(len(Lista)-1):
            if Lista[i] > Lista[i + 1]:
                Lista[i], Lista[i + 1] = Lista[i + 1], Lista[i]
                ordenado = False

    return Lista

#InsertionSort 
def InsertionSort(Lista):
    for i in range(1, len(Lista)):
        chave = Lista[i]
        j = i-1
        while j >= 0 and chave < Lista[j]:
            Lista[j + 1] = Lista[j]
            j -= 1
        Lista[j + 1] = chave

    return Lista

#ShellSort
def ShellSort(Lista):
    h = 1
    n = len(Lista)

    while h > 0:
            for i in range(h, n):
                c = Lista[i]
                j = i
                while j >= h and c < Lista[j - h]:
                    Lista[j] = Lista[j - h]
                    j = j - h
                    Lista[j] = c
            h = int(h / 2.2)

    return Lista

#QuickSort
def particao(lista, anterior, posterior):
    i = (anterior - 1)
    pivo = lista[posterior]

    for j in range(anterior, posterior):
        if lista[j] <= pivo:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[posterior] = lista[posterior], lista[i + 1]
    return (i + 1)

def QuickSort(lista, anterior, posterior):
    if anterior < posterior:
        pi = particao(lista, anterior, posterior)
        QuickSort(lista, anterior, pi - 1)
        QuickSort(lista, pi + 1, posterior)

    return lista

#MergeSort
def MergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)//2

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]
        MergeSort(listaDaEsquerda)
        MergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):
            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):
            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista

def criarLista():
    for i in range(20000):
        num = random.randint(1, 5000)
        Lista.append(num)

def contador(int):
    print("Ordenando...")
    tempoInic = time.time()
    if int == 1:
        print("BubbleSort...")
        BubbleSort(Lista.copy())
    elif int == 2:
        print("InsertionSort...")
        InsertionSort(Lista.copy())
    elif int == 3:
        print("ShellSort...")
        ShellSort(Lista.copy())
    elif int == 4:
        print("QuickSort...")
        QuickSort(Lista.copy(), 0, len(Lista)-1)
    elif int == 5:
        print("MergeSort...")
        MergeSort(Lista.copy())
    tempoFim = time.time()
    tempoTotal = tempoFim - tempoInic
    print(f'Tempo {round(tempoTotal*1000, 3)} ms')

#####################################################

criarLista()

while True:
    print('''
1 - BubbleSort
2 - InsertionSort
3 - ShellSort
4 - QuickSort
5 - MergeSort
6 - Todos de uma vez
7 - Sair''')
    teste = int(input("Escolha uma opção: "))

    if teste == 1:
        contador(teste)
    elif teste == 2:
        contador(teste)
    elif teste == 3:
        contador(teste)
    elif teste == 4:
        contador(teste)
    elif teste == 5:
        contador(teste)
    elif teste == 6:
        contador(1)
        contador(2)
        contador(3)
        contador(4)
        contador(5)
    elif teste == 7:
        print("Programa finalizado!")
        break