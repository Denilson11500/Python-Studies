import random
from time import time

print('Se tamanho menor ou igual a 10, será mostrado o passo a passo do processo.')
n = int(input('Digite o tamanho do array a ser organizado: '))


def bubble_sort(v):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(v) - 1):
            if v[i] > v[i + 1]:
                v[i], v[i + 1] = v[i + 1], v[i]
                if n <= 10:
                    print(v)
                sorted = False


def quick_sort(v, start, end):
    half = (start + end) // 2
    pivo = v[half]
    i, j = start, end
    while i < j:
        while v[i] < pivo:
            i += 1
        while pivo < v[j]:
            j -= 1
        if i < j:
            v[i], v[j] = v[j], v[i]
            if n <= 10:
                print(v)
            i += 1
            j -= 1
        elif i == j:
            i += 1
            j -= 1
    if start < j:
        quick_sort(v, start, j)
    if end > i:
        quick_sort(v, i, end)


def merge(v, start, half, end):
    t1 = half - start + 1
    t2 = end - half
    k = start
    v1 = []
    v2 = []
    for i in range(0, t1):
        v1.append(v[start + i])
    for i in range(0, t2):
        v2.append(v[half + 1 + i])
    i, j = 0, 0
    while i < t1 and j < t2:
        if v1[i] <= v2[j]:
            v[k] = v1[i]
            i += 1
        else:
            v[k] = v2[j]
            j += 1
        k += 1
    while i < t1:
        v[k] = v1[i]
        i += 1
        k += 1
    while j < t2:
        v[k] = v2[j]
        j += 1
        k += 1
    if n <=10:
        print(f'{v1} + {v2} = {v[start:end+1]}')


def merge_sort(v, start, end):
    if start < end:
        half = (start + end) // 2
        merge_sort(v, start, half)
        merge_sort(v, half + 1, end)
        merge(v, start, half, end)


def i_father(i):
    return i//2 - 1


def i_left_son(i):
    return 2*i + 1


def shift_down(v, start, end):
    root = start
    while i_left_son(root) <= end:
        child = i_left_son(root)
        swap = root
        if v[swap] < v[child]:
            swap = child
        if child + 1 <= end and v[swap] < v[child+1]:
            swap = child + 1
        if swap == root:
            return
        else:
            v[root], v[swap] = v[swap], v[root]
            if n <= 10:
                print(v)
            root = swap


def heapify(v, length):
    start = i_father(length - 1)
    while start >= 0:
        shift_down(v, start, length - 1)
        start -= 1


def heap_sort(v, length):
    end = length - 1
    heapify(v, length)
    while end > 0:
        v[0], v[end] = v[end], v[0]
        if n <= 10:
            print(v)
        end -= 1
        shift_down(v, 0, end)


array = []
array2 = []
array3 = []
array4 = []

for i in range(n):
    array.append(random.randrange(0, n + 1))
    array2.append(array[i])
    array3.append(array[i])
    array4.append(array[i])

print(f'Vetor aleatório de tamanho {n} :\m')
print(f'\nExecutando bubble sort, é lento para tamanhos muito grande:\n{array}')
if n <= 10:
    print('Exibido o vetor após cada troca.')
t0 = time()
bubble_sort(array)
tf = time()
print(f'Usando bubble sort:\n{array}')
print(f'Tempo usando bubble sort: {tf-t0}')
print(f'\nExecutando quick sort:\n{array2}')
if n <= 10:
    print('Exibido o vetor após cada troca, atenção pode ocorrer trocas de um elemento com ele mesmo.')
t0 = time()
quick_sort(array2, 0, len(array2)-1)
tf = time()
print(f'Usando quick sort:\n{array2}')
print(f'Tempo usando quick sort: {tf-t0}')
print(f'\nExecutando merge sort:\n{array3}')
if n <= 10:
    print('Exibido o vetor após cada merge, pode ser que nada seja alterado.')
t0 = time()
merge_sort(array3, 0, len(array3)-1)
tf = time()
print(f'Usando merge sort:\n{array3}')
print(f'Tempo usando merge sort: {tf-t0}')
print(f'\nExecutando heap sort:\n{array4}')
if n <= 10:
    print('Exibido o vetor após cada troca.')
t0 = time()
heap_sort(array4, len(array4))
tf = time()
print(f'Usando heap sort:\n{array2}')
print(f'Tempo usando heap sort: {tf-t0}')
