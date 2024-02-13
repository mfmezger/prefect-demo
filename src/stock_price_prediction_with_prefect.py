from prefect import task, Flow
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np


@task
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data


@task
def preprocess_data(data):
    data['Previous Day Price'] = data['Close'].shift(1)
    data = data.dropna()
    X = data[['Previous Day Price']]
    y = data['Close']
    return X, y


@task
def split_data(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=0)


@task
def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model


@task
def predict(model, X_test):
    return model.predict(X_test)


@task
def calculate_mse(y_test, y_pred):
    return mean_squared_error(y_test, y_pred)


@task
def predict_next_day_price(model, last_day_price):
    return model.predict(np.array(last_day_price).reshape(-1, 1))


with Flow("Stock Price Prediction Flow") as flow:
    data = fetch_stock_data("AAPL", "2020-01-01", "2023-01-01")
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_model(X_train, y_train)
    y_pred = predict(model, X_test)
    mse = calculate_mse(y_test, y_pred)
    next_day_price = predict_next_day_price(model, data['Close'][-1])

# flow executor
flow.run()
