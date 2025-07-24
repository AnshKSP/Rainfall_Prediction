from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Load and prepare data
df = pd.read_csv("Rainfall.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Normalize the dates to end on today
latest_csv_date = df['Date'].max().date()
today = datetime.today().date()
shift_days = (today - latest_csv_date).days
df['Date'] = df['Date'] + timedelta(days=shift_days)

# Train a model for each city
models = {}
for city in df['City'].unique():
    city_df = df[df['City'] == city].copy()
    city_df = city_df.sort_values('Date')
    city_df['DayIndex'] = (city_df['Date'] - city_df['Date'].min()).dt.days

    X = city_df[['DayIndex']]
    y = city_df['Rainfall']

    model = LinearRegression()
    model.fit(X, y)

    latest_temp = float(city_df['Temperature'].iloc[-1])
    latest_humidity = int(city_df['Humidity'].iloc[-1])
    latest_wind = float(city_df['WindSpeed'].iloc[-1])
    base_day_index = city_df['DayIndex'].max() + 1

    models[city] = {
        'model': model,
        'base_day_index': base_day_index,
        'latest_temp': latest_temp,
        'latest_humidity': latest_humidity,
        'latest_wind': latest_wind
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    city = request.args.get("city", "Delhi")
    days = int(request.args.get("days", 5))

    if city not in models:
        return jsonify({"error": "City not found"}), 404

    model_data = models[city]
    model = model_data['model']
    base_index = model_data['base_day_index']

    result = []
    for i in range(days):
        day_index = base_index + i
        pred = model.predict([[day_index]])[0]
        future_date = today + timedelta(days=i)

        result.append({
            'date': future_date.strftime('%Y-%m-%d'),
            'predicted_rainfall': round(float(pred), 2),
            'temperature': model_data['latest_temp'],
            'humidity': model_data['latest_humidity'],
            'wind_speed': model_data['latest_wind']
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
