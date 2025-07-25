# Rainfall Forecast Web App 🌧️

This project is a web application that predicts future rainfall for various cities in India. It uses a simple linear regression model trained on historical data to provide forecasts for the upcoming days.

## ✨ Features

* **City-Specific Forecasts:** Get rainfall predictions for multiple major cities across India.
* **Multi-Day Prediction:** Choose to forecast for 1, 3, or 5 days.
* **Real-time Data Fetching:** The frontend dynamically fetches predictions from the backend API without needing to reload the page.
* **Clean & Simple UI:** A user-friendly interface built with Bootstrap for a smooth experience.
* **Additional Weather Info:** Along with rainfall, the app displays the latest recorded temperature, humidity, and wind speed for the selected city.

## 🛠️ How It Works

The application consists of a Python Flask backend and an HTML/JavaScript frontend.

1.  **Data Preparation:**
    * The application loads historical weather data from `Rainfall.csv`.
    * For each city, it creates a separate `LinearRegression` model.
    * The dates in the dataset are normalized to ensure the forecast starts from the current day.

2.  **Backend (Flask - `app.py`):**
    * A Flask server is set up to handle requests.
    * The main route `/` serves the `index.html` file.
    * The `/predict` API endpoint takes a `city` and the number of `days` as query parameters.
    * It uses the corresponding city's trained model to predict rainfall for the requested number of future days.
    * The predictions, along with other weather data, are returned as a JSON response.

3.  **Frontend (`index.html`):**
    * A simple webpage with dropdowns for selecting a city and the number of forecast days.
    * When the "Get Prediction" button is clicked, a JavaScript function sends a `fetch` request to the backend `/predict` endpoint.
    * The returned JSON data is then dynamically rendered on the page, showing the forecast for each day in a separate card.

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need Python and pip installed on your machine.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Create a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required packages:**
    Create a `requirements.txt` file with the following content:
    ```
    Flask
    Flask-Cors
    pandas
    scikit-learn
    numpy
    ```
    Then run the installation command:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1.  Place your `Rainfall.csv` file in the root directory of the project.
2.  Run the Flask application:
    ```sh
    python app.py
    ```
3.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 📂 File Structure

```
.
├── app.py             # The main Flask application script
├── templates
│   └── index.html     # The single-page frontend
└── Rainfall.csv       # The dataset with historical rainfall data

```
### 🚀 Run It

Install the required packages:

```bash
pip install -r requirements.txt
```
