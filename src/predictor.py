from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def train_model(data):

    X = data[['Open','High','Low','Volume']]
    y = data['Close']

    X_train,X_test,y_train,y_test = train_test_split(
        X,y,test_size=0.2,shuffle=False
    )

    model = LinearRegression()

    model.fit(X_train,y_train)

    return model
def predict_price(model,data):

    latest = data[['Open','High','Low','Volume']].tail(1)

    prediction = model.predict(latest)

    return prediction[0]