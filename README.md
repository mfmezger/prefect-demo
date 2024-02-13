
# Stock Price Prediction with Python, yfinance, and Prefect

This project demonstrates a basic approach to predict stock prices using Python, `yfinance` for fetching historical stock data, and Prefect for orchestrating the data pipeline.

## Description

The script fetches historical stock data using the `yfinance` library, processes the data, and applies a simple linear regression model to predict future stock prices. The process is organized into a pipeline managed by Prefect, a powerful workflow management system.

## Prerequisites

Before running this project, ensure you have the following installed:
- Python (3.7 or later)
- Pip (Python package installer)

## Installation

1. **Clone the Repository**
   ```
   git clone <repository-url>
   ```
2. **Install Required Libraries**
   Use pip to install the required Python libraries:
   ```
   pip install yfinance sklearn prefect
   ```

## Usage

To run the stock price prediction pipeline, execute the main script:

```
python stock_price_prediction.py
```

This script will perform the following tasks:
- Fetch historical stock data for a specified ticker (default is AAPL).
- Preprocess the data for modeling.
- Train a simple linear regression model.
- Predict future stock prices.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
