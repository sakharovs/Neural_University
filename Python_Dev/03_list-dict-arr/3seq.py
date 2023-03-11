list1 = input('Введите эл-ты первого списка через запятую: ').split(',')
list1 = [int(x) for x in list1]
list2 = input('Введите эл-ты второго списка через запятую: ').split(',')
list2 = [int(x) for x in list2]
list1 = [x for x in list1 if x not in list2]
print('Результат ', *list1, sep=',')