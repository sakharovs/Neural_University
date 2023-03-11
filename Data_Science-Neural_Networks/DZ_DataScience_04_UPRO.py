"""
Используя базу "Пассажиры автобуса", подготовьте данные для обучения нейронной сети, классифицирующей изображение на два класса:
входящий пассажир
выходящий пассажир
Добейтесь точности работы модели на проверочной выборке не ниже 85%
"""
# Импортируем библиотеки
import numpy as np
import wget as wget
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import load_img
from tensorflow.keras import utils
from sklearn.model_selection import train_test_split
from keras.preprocessing import image
import matplotlib.pyplot as plt
import gdown, os, random
import zipfile

import tensorflow as tf
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(gpus[0],
            [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    except RuntimeError as e:
        print(e)

# загрузка и разархивирование базы в папку 'bus'
# gdown.download('https://storage.yandexcloud.net/aiueducation/Content/base/l4/bus.zip', None, quiet = True)
# with zipfile.ZipFile('bus.zip', 'r') as zip_ref:
#     zip_ref.extractall(os.path.join(os.getcwd(), 'bus'))

# Создание переменных  для хранения путей к папкам и файлам базы
dir_bus = os.listdir(os.path.join(os.getcwd(), 'bus'))
path_in = os.path.join(os.getcwd(), 'bus', dir_bus[0])
path_out = os.path.join(os.getcwd(), 'bus', dir_bus[1])

print(path_in)
print(path_out)

print('Входящий')
image_name = random.choice(os.listdir(path_in))
tmp_image = load_img(os.path.join(path_in, image_name), target_size=(128, 64))
plt.imshow(tmp_image)
plt.show()

print('Выходящий')
image_name = random.choice(os.listdir(path_out))
tmp_image = load_img(os.path.join(path_out, image_name), target_size=(128, 64))
plt.imshow(tmp_image)
plt.show()

# Подготовка выборки
x_data = []
y_data = []

for fn in os.listdir(path_in):
  im = np.array(load_img(os.path.join(path_in, fn), target_size=(128,64)))
  x_data.append(im)
  y_data.append(0)

for fn in os.listdir(path_out):
  im = np.array(load_img(os.path.join(path_out, fn), target_size=(128,64)))
  x_data.append(im)
  y_data.append(1)

x_data = np.array(x_data)
y_data = np.array(y_data)

print(x_data.shape)
print(y_data.shape)

# Нормализация данных
x_data_reshape = x_data.reshape(-1, 128*64*3) / 255.
print(x_data_reshape.shape)

# Деление на обучающую и тестовую выборки
x_train, x_val, y_train, y_val = train_test_split(x_data_reshape,
                                                  y_data,
                                                  test_size=0.2,
                                                  shuffle=True,
                                                  random_state=3)
print('Размеры сформированных массивов:')

print(x_train.shape)
print(x_val.shape)
print(y_train.shape)
print(y_val.shape)

# Формирование и обучение НС
model = Sequential()

model.add(Dense(2048, input_dim=x_train.shape[1], activation='relu', name="Inbound"))
model.add(Dense(800, activation='relu', name='First_hidden'))
model.add(Dense(1, activation='sigmoid', name='Outbound'))

model.summary()

from sklearn.utils import validation
model.compile(optimizer=Adam(learning_rate=0.0001),
              metrics=['accuracy'],
              loss='binary_crossentropy')

history = model.fit(x_train,
                    y_train,
                    validation_data=(x_val, y_val),
                    epochs=50,
                    batch_size=128)

plt.plot(history.history['accuracy'], label='Точность')
plt.plot(history.history['val_accuracy'], label='Точность на проверочной')
plt.legend()
plt.show()

plt.plot(history.history['loss'], label='Потери')
plt.plot(history.history['val_loss'], label='Потери на проверочной')
plt.legend()
plt.show()

# Точность модели
scores = model.evaluate(x_train, y_train)
print(f'Точность на обучающей выборке:', scores[1]*100,'%'  )

scores = model.evaluate(x_val, y_val)
print(f'Точность на проверочной выборке:',scores[1]*100, '%' )