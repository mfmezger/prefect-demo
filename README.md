
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

## Setup Steps

1. **Install Prefect**: Install Prefect Python library using pip.
   ```
   pip install prefect
   ```

2. **Start Prefect Server and UI**:
   - Prefect Server can be started using Docker.
   - Use Prefect CLI to spin up the server and UI.
     ```
     prefect server start
     ```

3. **Configure Database**:
   - Connect Prefect Server to a PostgreSQL database.
   - The connection can be configured via the Prefect CLI or environment variables.

4. **Start an Agent**:
   - Run a Prefect agent in your environment.
     ```
     prefect agent start
     ```

5. **Deploy and Run Flows**:
   - Write flows as you would in Prefect Cloud.
   - Register flows to your on-premise server.
   - Trigger runs through the UI or Prefect CLI.

For detailed installation and configuration instructions, refer to the [Prefect Documentation](https://docs.prefect.io/orchestration/server/overview.html).


## Simple Usage without Prefect

To run the stock price prediction pipeline, execute the main script:

```
python stock_price_prediction.py
```

This script will perform the following tasks:
- Fetch historical stock data for a specified ticker (default is AAPL).
- Preprocess the data for modeling.
- Train a simple linear regression model.
- Predict future stock prices.

## Usage with Prefect

To run the stock price prediction pipeline using Prefect, execute the following command:

Prefect On-Premise is a deployment option for Prefect, allowing you to run and manage Prefect within your own infrastructure. This guide provides a simplified overview of setting up and using Prefect in an on-premise environment.

This is ideal for those who want to maintain control over their data and execution environment. It involves setting up Prefect's components within your own servers or private cloud.

1. **Start Prefect Server and UI**:
   - Prefect Server can be started using Docker.
   - Use Prefect CLI to spin up the server and UI.
     ```
     prefect server start
     ```

2. **Configure Database**:
   - Connect Prefect Server to a PostgreSQL database.
   - The connection can be configured via the Prefect CLI or environment variables.


3. **Start an Agent**:
   - Run a Prefect agent in your environment.
     ```
     prefect agent start
     ```

4. **Deploy and Run Flows**:
   - Write flows as you would in Prefect Cloud.
   - Register flows to your on-premise server.
   - Trigger runs through the UI or Prefect CLI.
   
   

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).
