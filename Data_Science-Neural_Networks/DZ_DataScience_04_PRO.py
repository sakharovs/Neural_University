# Последовательная модель НС
from tensorflow.keras.models import Sequential
# Основные слои
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization
# Утилиты для to_categorical()
from tensorflow.keras import utils
# Алгоритмы оптимизации для обучения модели
from tensorflow.keras.optimizers import Adam
# Библиотека для работы с массивами
import numpy as np
# Отрисовка графиков
import matplotlib.pyplot as plt
# Разделение данных на выборки
from sklearn.model_selection import train_test_split
# Для загрузки датасета
from sklearn.datasets import load_wine


x_data = load_wine()['data']              # Загрузка набора данных о винах
y_data = load_wine()['target']            # Загрузка классов вин

print('Размерность x_data -', x_data.shape)
print('Размерность y_data -', y_data.shape)
print()

# Вывод примера данных
print('Данные по первому вину:',x_data[177])
print('Класс вина:',y_data[177])

# Перевод в one hot encoding
y_data = utils.to_categorical(y_data, 3)

# Разбиение наборов на общую и тестовую выборки
x_all, x_test, y_all, y_test = train_test_split(x_data,
                                                y_data,
                                                test_size=0.1,
                                                shuffle=True,
                                                random_state = 6)

# Разбиение общей выборки на обучающую и проверочную
x_train, x_val, y_train, y_val = train_test_split(x_all,
                                                  y_all,
                                                  test_size=0.1,
                                                  shuffle=True,
                                                  random_state = 6)

print('x_train', x_train.shape)
print('y_train', y_train.shape)

print('x_val', x_val.shape)
print('y_val', y_val.shape)

# Создание модели
model = Sequential()

model.add(Dense(100, input_dim=x_train.shape[1], activation='relu'))
model.add(Dense(10,  activation='relu'))
model.add(Dense(3, activation='relu'))

model.summary()

# Компиляция
model.compile(optimizer=Adam(learning_rate=0.001),
              metrics=['accuracy'],
              loss='categorical_crossentropy')

# Обучение модели
history = model.fit(x_train,
                    y_train,
                    validation_data=(x_val, y_val),
                    epochs=500,
                    batch_size = 32)

# Вывод графика обучения
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.show()

model.evaluate(x_test, y_test)