# Считываем список A
list_A = list(map(int, input().split()))

# Считываем список B
list_B = list(map(int, input().split()))

# Сортируем списки
list_A.sort()
list_B.sort()

# Инициализируем счетчик совпадающих чисел
count = 0

# Используем два указателя для обхода списков
index_A = index_B = 0

# Используем цикл while для сравнения элементов списков
while index_A < len(list_A) and index_B < len(list_B):
    if list_A[index_A] < list_B[index_B]:
        index_A += 1
    elif list_B[index_B] < list_A[index_A]:
        index_B += 1
    else: # если элементы равны
        count += 1
        index_A += 1
        index_B += 1

# Если после цикла while есть дополнительные совпадения в первом списке,
# добавляем их в счетчик
while index_A < len(list_A):
    if list_A[index_A] == list_B[index_B - 1]:
        count += 1
    index_A += 1

# Выводим счетчик совпадающих чисел
print(count)