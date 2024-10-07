def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

generator = get_number()

for id, num in enumerate(generator, start=1):
    if id == 1:
        first = num
    if id == 5:
        fifth = num
    last = num

# Выводим результаты
print(f"Первое нечётное число: {first}")
print(f"Пятое нечётное число: {fifth}")
print(f"Последнее нечётное число: {last}")
