from datetime import datetime

def calculate_age():
    birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
    try:
        birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
                age -= 1
        print(f"Ваш возраст: {age} лет")
    except ValueError:
            print ('Неправильный ввод даты')

calculate_age()