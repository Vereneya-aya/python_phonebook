from return_data_file import data_file

def copy_row():
    print("Выберите файл, из которого хотите копировать контакт: ")
    data_from, nf_from = data_file()
    count_rows = len(data_from)
    number_row = int(input(f"Введите номер строку, которую хотите копировать: "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    print("Выберите файл, в который хотите копировать контакт: ")
    data_to, nf_to = data_file()
    number_row_to = len(data_to) + 1
    with open(f'db/phonebook{nf_from}.txt', 'r', encoding='utf-8') as file:
            data_to_copy = f"{number_row_to};{data_from[number_row-1].split(";")[1]};{data_from[number_row-1].split(";")[2]};{data_from[number_row-1].split(";")[3]};{data_from[number_row-1].split(";")[4]}"
    with open(f'db/phonebook{nf_to}.txt', 'a', encoding='utf-8') as file:
        file.write(f'{data_to_copy}\n')
    print("Данные успешно копированы!")
    
