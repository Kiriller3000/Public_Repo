#Функция быстрой сортировки
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)

# Функция двоичного поиска
def binary_search(array, element, left, right):
    #if left > right:
    #    return False
    middle = (right + left) // 2
    if element <= array[0]:
        return -1
    elif array[end_index] < element:
        return end_index
    elif array[middle] <= element <= array[middle+1]:
        return middle-1 if element == array[middle] else middle # Если введенное число равно предыдущему в массиве, берем предшествующую ему позицию
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

while True:
    try:
        array = list(map(int, input('Введите массив числовых значений через пробел и нажмите enter\n').split()))
        if not array:
            print('Массив пустой')
            continue
    except ValueError as error:
        print('Введите числовые значения!\n')
    else:
        break

end_index = len(array)-1 # Индекс последнего элемента O(n) Вычисляем один раз в программе
qsort(array, 0, end_index)
print(array)

while True:
    try:
        number = int(input(f'Введите число в диапазоне:  {array[0]} - {array[end_index]}: '))
        if number < array[0] or number > array[end_index]:
            print('Неверный ввод: число вне диапазона\n')
            continue
    except ValueError as error:
        print('Введите число!\n')
    else:
        break

prev_index = binary_search(array, number, 0, end_index)
print(f'Предшествующая введенному числу позиция: {prev_index+1}')# Позиция - +1 к индексу
