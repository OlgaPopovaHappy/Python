# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.
# in Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in Number of words: -1
# out
# The data is incorrect

import random

def get_offer(user_number):
    word = 'абв'
    result = []
    for i in range(user_number):
        temp = random.sample(word, k = 3)
        result.append(''.join(temp))
    my_list = ' '.join(result)
    print(my_list)
    return my_list

def clean_list(line):
    word = 'абв'
    line = line.split(' ')
    for i in line:
        if word in line:
            line.remove(word)
    new_list = ' '.join(line)
    return new_list

print(clean_list(get_offer(int(input('Количество слов: ')))))




#     for x in line:
#         for y in line:
#             for z in line:
#                 print(line)


# # n = random.choices(line)
# # print(line)
# # print(n)

# # a = "авб абв бав абв вба бав вба абв абв абв"



# # b = a.replace("абв", "")
# # print(b.replace("  ", " "))

# # text = 'ваб вба абв орп бва абв'
# # print(text)


# # def del_some_words(text):
# #     text = list(filter(lambda x: 'абв' not in x, text.split()))
# #     return " ".join(text)


# text = del_some_words(text)
# print(text)