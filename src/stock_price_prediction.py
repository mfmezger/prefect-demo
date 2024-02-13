import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

ticker = "AAPL"


def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


def preprocess_data(data):
    data = data[['Close']]
    data['Previous Day Price'] = data['Close'].shift(1)
    data = data.dropna()
    return data


def split_data(data):
    X = data[['Previous Day Price']]
    y = data['Close']
    return X, y


def split_train_test(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    return X_train, X_test, y_train, y_test


def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


def predict(model, X_test):
    return model.predict(X_test)


def calculate_mse(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)


def predict_next_day_price(model, data):
    last_day_price = np.array(data['Close'][-1]).reshape(-1, 1)
    next_day_price = model.predict(last_day_price)
    return next_day_price[0]
