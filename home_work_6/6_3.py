# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
# ключи — первые буквы имён, значения — списки, содержащие имена,
# начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


def assignment(names):
    names.sort()
    as_keys = [i[0] for i in names]
    keys = []
    for i in range(len(as_keys)):
        if not as_keys[i] in keys:
            keys.append(as_keys[i])
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = []
    for key in range(len(keys)):
        for name in range(len(names)):
            if names[name][0] == keys[key]:
                dic[keys[key]].append(names[name])
    return dic


# names=input('Имена сотрудников, через запятую: ').split(',')
names = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]

print(assignment(names))
