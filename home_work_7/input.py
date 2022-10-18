def get_info():
    info = []
    name = input('Введите фимилию: ')
    if len(name) > 2:
        if name.isalpha():
            info.append(name)
            name = input('Введите имя: ')
            if len(name) > 2:
                if name.isalpha():
                    info.append(name)
                    tel = input('Введите номер телефона: ')
                    if len(tel) > 4:
                        if tel.isdigit():
                            info.append(tel)
                            description = input('Введите описание: ')
                            info.append(description)
                        else:
                            print(f'Номер телефона не может состоять из букв!')
                    else:
                        print(f'Вы допустили ошибку при вводе номера телефона')
                else:
                    print(f'В имени вы допустили ошибку.')
            else:
                print(f'Вы допустили ошибку при вводе имени')
        else:
            print(f'Вы допустили ошибку при вводе фамилии')
    else:
        print(f'Вы допустили ошибку при вводе фамилии')
    return info


