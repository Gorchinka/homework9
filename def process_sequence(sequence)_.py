def process_sequence(sequence):
    numbers_seen = set()
    for number in sequence:
        if number in numbers_seen:
            print("YES")
        else:
            print("NO")
            numbers_seen.add(number)

# Ввод данных
sequence = list(map(int, input().split()))

# Вызов функции для обработки последовательности
process_sequence(sequence)