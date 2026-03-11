import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def prepare_lstm_data(data):

    close_prices = data['Close'].values.reshape(-1,1)

    scaler = MinMaxScaler(feature_range=(0,1))

    scaled_data = scaler.fit_transform(close_prices)

    X = []
    y = []

    for i in range(60, len(scaled_data)):

        X.append(scaled_data[i-60:i])
        y.append(scaled_data[i])

    X = np.array(X)
    y = np.array(y)

    return X,y,scaler


def build_lstm_model():

    model = Sequential()

    model.add(LSTM(50, return_sequences=True, input_shape=(60,1)))

    model.add(LSTM(50))

    model.add(Dense(1))

    model.compile(
        optimizer='adam',
        loss='mean_squared_error'
    )

    return model
def train_lstm(data):

    X,y,scaler = prepare_lstm_data(data)

    model = build_lstm_model()

    model.fit(
        X,
        y,
        epochs=5,
        batch_size=32
    )

    return model, scaler
def predict_next_price(model, scaler, data):

    close_prices = data['Close'].values.reshape(-1,1)

    scaled = scaler.transform(close_prices)

    last_60 = scaled[-60:]

    X_test = last_60.reshape(1,60,1)

    predicted = model.predict(X_test)

    predicted_price = scaler.inverse_transform(predicted)

    return predicted_price[0][0]