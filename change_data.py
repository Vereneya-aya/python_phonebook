from return_data_file import data_file


def change_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    name = input("Введите свое имя: ")
    surname = input("Input surname: ")
    patronymic = input("Input patronymic: ")
    phone_number = input("Input phone number: ")
    data[number_row - 1] = f'{number_row};{name};{surname};{patronymic};{phone_number}\n'
    with open(f'db/phonebook{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")
