# Rainfall Prediction API

A simple Flask-based web API that predicts future rainfall for various cities using a linear regression model. The application reads historical weather data from a CSV file, trains a unique model for each city, and exposes an endpoint to get future rainfall predictions.

## Features

-   **Dynamic Date Adjustment**: Automatically shifts the historical data timeline to end on the current day, ensuring predictions are always for the immediate future.
-   **Multi-City Support**: Trains a separate machine learning model for each city found in the dataset.
-   **Simple API Endpoint**: Provides a clean `GET` endpoint to fetch predictions.
-   **Customizable Forecast**: Allows users to specify the city and the number of days to forecast.
-   **CORS Enabled**: `Flask-CORS` is integrated for easy access from a web frontend running on a different domain.

## How It Works

The application follows these steps upon startup:

1.  **Data Loading**: It loads a `Rainfall.csv` file into a Pandas DataFrame.
2.  **Date Normalization**: It finds the most recent date in the CSV file and calculates the difference to today's date. All dates in the dataset are then shifted forward by this difference. This ensures the model's predictions start from tomorrow, regardless of how old the data is.
3.  **Model Training**:
    -   For each unique `City` in the dataset, a new `LinearRegression` model is trained.
    -   A `DayIndex` (number of days since the start of the dataset) is created to be used as the single feature (`X`) for the model.
    -   The model learns to predict `Rainfall` (`y`) based on this `DayIndex`.
    -   The trained model and other relevant data (like the latest temperature, humidity, and wind speed) are stored in memory.
4.  **API Endpoint**:
    -   A single endpoint `/predict` is exposed.
    -   When a request is received, it uses the pre-trained model for the requested city to predict rainfall for the specified number of future days.
    -   The predictions for temperature, humidity, and wind speed are currently static and based on the last known values from the CSV for that city.

## Setup and Installation

Follow these instructions to get the project running on your local machine.

### Prerequisites

-   Python 3.7+
-   `pip` (Python package installer)

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    Create a `requirements.txt` file with the following content:
    ```
    Flask
    Flask-Cors
    pandas
    numpy
    scikit-learn
    ```
    Then, install the packages from the file:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Add the data file:**
    Place your `Rainfall.csv` file in the root directory of the project. The CSV must contain the following columns: `Date`, `City`, `Rainfall`, `Temperature`, `Humidity`, and `WindSpeed`.

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The application will start in debug mode on `http://127.0.0.1:5000`.

## API Usage

### Endpoint: `GET /predict`

Returns rainfall predictions for a given city for a specified number of days.

**Query Parameters:**

| Parameter | Type    | Description                                       | Default |
|-----------|---------|---------------------------------------------------|---------|
| `city`    | string  | The name of the city to predict.                  | `Delhi` |
| `days`    | integer | The number of future days to predict.             | `5`     |

---

**Example Request:**

You can use `curl` or any web browser to make a request.

```bash
curl "[http://127.0.0.1:5000/predict?city=Mumbai&days=7](http://127.0.0.1:5000/predict?city=Mumbai&days=7)"
```
# Limitations and Future Improvements

1.  **Simple Model**: The current LinearRegression model only uses the day index as a feature.        This is a simplification and may not capture complex weather patterns.

    **Improvement**: Use more sophisticated time-series models like ARIMA, SARIMAX, or                recurrent neural networks (LSTM).

2.  **Static Features**: Temperature, humidity, and wind speed are not predicted; they are            static values from the last available data point.

    **Improvement**: Train separate models to predict these features as well.

3.  **Data Source**: The app relies on a local CSV file loaded into memory.

    **Improvement**: Connect the application to a database for more robust data management and        scalability.

4.  **No Model Persistence**: Models are retrained every time the app starts.

    **Improvement**: Save trained models to disk (e.g., using joblib or pickle) to avoid              retraining on every launch.

5.  **Configuration**: Key values like the data file name (Rainfall.csv) are hardcoded.

    **Improvement**: Move settings into a separate configuration file or use environment            variables to make the application more flexible.

6.  **Error Handling**: The current error handling is minimal. The app may crash if the CSV is      not found or if the input data is malformed.

    **Improvement**: Add comprehensive try-except blocks and validation to handle potential         issues gracefully (e.g., file not found, missing columns, invalid query parameters).

7.  **Testing**: The project lacks an automated test suite.

    **Improvement**: Implement unit tests (using pytest or unittest) to verify the logic of         individual functions and integration tests to validate the API endpoints.
