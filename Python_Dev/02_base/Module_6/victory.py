pushkin_birth_year = 0  # год рождения Пушкина 1799
putin_birth_year = 0  # год рождения Путина 1952
sakharov_birth_year = 0  # год рождения Сахарова 1921
tesla_birth_year = 0  # год рождения Теслы 1856
jobs_birth_year = 0  # год рождения Джобса 1955

answer = None
while answer != 'НЕТ':
    count_right = 0
    count_wrong = 0
    print("Привет! Сейчас будет 5 вопросов. Каждый вопрос - это год рождения кого-то известного.")

    count_question = 0
    pushkin_birth_year = int(input('Введи год рождения Пушкина '))
    count_question+=1
    putin_birth_year = int(input('Введи год рождения Путина '))
    count_question += 1
    sakharov_birth_year = int(input('Введи год рождения академика Сахарова '))
    count_question += 1
    tesla_birth_year = int(input('Введи год рождения Николы Тесла '))
    count_question += 1
    jobs_birth_year = int(input('Введи год рождения Стива Джобса '))
    count_question += 1

    if pushkin_birth_year == 1799:
        count_right += 1
    else:
        count_wrong += 1
    if putin_birth_year == 1952:
        count_right += 1
    else:
        count_wrong += 1
    if sakharov_birth_year == 1921:
        count_right += 1
    else:
        count_wrong += 1
    if tesla_birth_year == 1856:
        count_right += 1
    else:
        count_wrong += 1
    if jobs_birth_year == 1955:
        count_right += 1
    else:
        count_wrong += 1

    print('Всего вопросов - ', count_question)
    print('Правильных ответов ', count_right)
    print('Не правильных ответов ', count_wrong)

    print('Процент правильных ответов ', count_right * 100 / count_question, '%')
    print('Процент неправильных ответов ', 100 - (count_right * 100 / count_question), '%')
    answer = input('Хочешь еще попытку? (Да/Нет) ').upper()
