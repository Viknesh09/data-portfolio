# 🚖 RideFlow AI

## 📌 Project Overview

RideFlow AI is an AI-powered ride analytics platform designed to optimize ride-sharing operations through Machine Learning, NLP, and Intelligent Decision Systems.

The platform predicts ride demand, supply availability, dynamic pricing, cancellation risk, customer sentiment, and recommends optimal driver matching.

---

## 🎯 Problem Statement

Ride-sharing companies face several challenges:

- Demand fluctuations
- Driver shortages
- Ride cancellations
- Customer complaints
- Inefficient driver allocation

RideFlow AI addresses these challenges using Machine Learning and NLP.

---

## 🏗️ Architecture

![Architecture](architecture.png)

---

## 📊 Dataset

NYC Taxi Trip Dataset

Features used:

- pickup_hour
- PULocationID
- trip_distance
- fare_amount
- ETA
- traffic_level
- driver_rating
- surge_multiplier

Customer feedback dataset:

- feedback
- sentiment

---

## 🤖 Machine Learning Models

### 1. Demand Prediction

Model:
Random Forest Regressor

Inputs:

- pickup_hour
- PULocationID

Output:

- predicted_demand

---

### 2. Supply Prediction

Model:
Random Forest Regressor

Inputs:

- pickup_hour
- PULocationID

Output:

- predicted_supply

---

### 3. Dynamic Pricing

Logic:

Demand / Supply Ratio

Output:

- surge_multiplier
- recommended_fare

---

### 4. Cancellation Prediction

Model:
Random Forest Classifier

Features:

- ETA
- traffic_level
- driver_rating
- surge_multiplier
- trip_distance
- fare_amount

Output:

- cancellation probability
- risk level

---

## 🧠 NLP Module

### DistilBERT Sentiment Analysis

Input:

Customer Feedback

Output:

- Positive
- Negative

Performance:

Accuracy: 90.67%

---

## 🚕 Ride Matching Assistant

Uses:

- Demand
- Supply
- Driver Rating
- Cancellation Risk

Output:

- Match Score
- Recommendation

---

## 💬 AI Chatbot

Features:

- Booking support
- Refund queries
- Driver support
- Ride assistance

Languages:

- English
- Tamil
- Hindi

---

## ⚡ FastAPI Endpoints

### GET

- /

- /model_info

### POST

- /predict_demand
- /predict_supply
- /dynamic_pricing
- /predict_cancellation
- /predict_sentiment
- /ride_matching_assistant

---

## 📈 Streamlit Dashboard

Modules:

- Demand Prediction
- Dynamic Pricing
- Cancellation Prediction
- Sentiment Analysis
- Ride Matching Assistant
- Chatbot Support
- Analytics Dashboard

---

## 🛠️ Technology Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- DistilBERT
- Transformers
- FastAPI
- Streamlit
- Joblib

---

## 📂 Project Structure

ride_flow_ai/

├── app/

├── api/

├── models/

├── data/

├── notebooks/

├── architecture.png

└── README.md

---

## 🚀 Future Enhancements

- Real-time ride tracking
- Driver route optimization
- Deep Learning demand forecasting
- Voice-based chatbot
- Cloud deployment

---

## 👨‍💻 Author

Viknesh K

RideFlow AI Project