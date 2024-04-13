from return_data_file import data_file


def add_row():
    name = input("Input name: ")
    surname = input("Input surname: ")
    patronymic = input("Input patronymic: ")
    phone_number = input("Input phone number: ")
    data, nf = data_file()
    now_number_row = len(data) + 1
    with open(f'db/phonebook{nf}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row};{name};'
                   f'{surname};{patronymic};{phone_number}\n')
    print("Данные успешно записаны!")