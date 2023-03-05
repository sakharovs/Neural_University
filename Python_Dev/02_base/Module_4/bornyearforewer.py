born_year = ''
while born_year!=1799:
    born_year = int(input("Привет! Назови год рождения А.С.Пушкина: "))
    if born_year == 1799:
        print("Верно!")
    else:
        print('Неверно!')