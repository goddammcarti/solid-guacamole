import random
list = [random.randint(-10, 10) for i in range(10)]
copied_list = list[:]

copied_list.append('copied')

print('Список', list)
print('Скопированный список', copied_list)




