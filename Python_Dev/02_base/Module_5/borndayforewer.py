born_year = ''
born_day = ''
while born_year != 1799:
    born_year = int(input("Привет! Назови год рождения А.С.Пушкина: "))
    if born_year == 1799:
        print("Верно!")
        while born_day != 6:
            born_day = int(input('А число месяца какое? '))
            if born_day == 6:
                print("Верно!")
            else:
                 print('Неверный день рождения!')
    else:
        print('Неверный год!')
