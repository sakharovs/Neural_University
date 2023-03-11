from tensorflow.keras.models import Sequential
# Основные слои
from tensorflow.keras.layers import Dense, Activation, Dropout, BatchNormalization

def create_model(num_N, drop, norm=False):
    """
    Функция создает модель НС с заданными параметрами
    :param num_N: кол-во нейронов на вход
    :param drop: размер Dropout
    :param norm: добавление слоя BAtchNormalization. По умолчанию False
    :return: Созданная model.Sequental
    """
    model = Sequential()

    if norm:
        model.add(BatchNormalization(input_shape=(x_train.shape[1],)))
        model.add(Dense(num_N, actvation='relu'))
    else:
        model.add(Dense(num_N, input_dim=x_train.shape[1], activation='relu'))

    model.add(Dropout(drop))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_entropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    return model
