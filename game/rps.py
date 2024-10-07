import random

def options(num):
    if num == 1:
        print('Камень')
    elif num == 2:
        print('Ножницы')
    else:
        print('Бумага')
def game (choice):
    ai_choice = random.randint(0, 4)
    if choice == ai_choice:
        options(ai_choice)
        print('Ничья')
    elif (ai_choice == 1 and choice == 2) or (ai_choice == 2 and choice == 3) or (ai_choice == 3 and choice == 1):
        options(ai_choice)
        print('Поражение')
    else:
        options(ai_choice)
        print('Победа')


while True:

    print('1 - Камень')
    print('2 - Ножницы')
    print('3 - Бумага')
    print('4 или любая другое число - выход')
    choice = input("Ваш выбор: ")

    try:
        choice = int (choice)

        if choice >= 4:
            break
        else:
            game (choice)
    except ValueError:
        print('неправильный ввод')