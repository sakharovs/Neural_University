qty_elements = int(input("Введите кол-во эл-тов: "))
point_list = []
for i in range(qty_elements):
    z = int(input(f"Введите {i+1} эл - т: "))
    point_list.append(z)
point_list.sort()
print(f'Вывод: {point_list}')

