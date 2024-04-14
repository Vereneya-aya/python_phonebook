def find_row():
    flag = False
    contact_to_find = input("Введите имя или фамилию контакта для поиска: ")
    for j in range(1,3):
        with open(f'db/phonebook{j}.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for i in range(len(data)):
                if contact_to_find in data[i]:
                    flag = True
                    print(f'Вот контакт: {data[i]}\nВы можете удалить или изменить этот контакт, выбрав строку {i+1} в файле {j} после выбора соответствующей команды в стартовом меню\n')
    if not flag:
       print("Контакт не найден!")