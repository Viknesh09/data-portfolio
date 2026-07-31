from fastapi import FastAPI
import joblib
import pandas as pd
import traceback
from transformers import pipeline

app = FastAPI(
    title="RideFlow AI API",
    description="Ride Analytics & Prediction APIs",
    version="1.0"
)

# Load Demand Model
demand_model = joblib.load(
    r"D:\Guvi\Projects\ride_flow_ai\models\demand_prediction_model.pkl"
)

# Supply Model
supply_model = joblib.load(
    r"D:\Guvi\Projects\ride_flow_ai\models\supply_prediction_model.pkl"
)

# Load Cancellation Model
cancellation_model = joblib.load(
    r"D:\Guvi\Projects\ride_flow_ai\models\cancellation_prediction_model.pkl"
)

sentiment_pipeline = pipeline(
    "text-classification",
    model=r"D:\Guvi\Projects\ride_flow_ai\models\distilbert_sentiment_model",
    tokenizer=r"D:\Guvi\Projects\ride_flow_ai\models\distilbert_sentiment_model"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to RideFlow AI API",
        "status": "Running Successfully"
    }


@app.get("/model_info")
def model_info():
    try:
        info = {
            "n_features": int(demand_model.n_features_in_)
        }

        if hasattr(demand_model, "feature_names_in_"):
            info["feature_names"] = list(
                demand_model.feature_names_in_
            )

        return info

    except Exception as e:
        return {"error": str(e)}


@app.post("/predict_demand")
def predict_demand(
    pickup_hour: int,
    PULocationID: int
):
    try:

        features = pd.DataFrame(
            [[PULocationID, pickup_hour]],
            columns=[
                "PULocationID",
                "pickup_hour"
            ]
        )

        prediction = demand_model.predict(features)[0]

        return {
            "pickup_hour": pickup_hour,
            "PULocationID": PULocationID,
            "predicted_demand": float(prediction)
        }

    except Exception as e:

        return {
            "error": str(e)
        }
    
@app.post("/predict_supply")
def predict_supply(
    pickup_hour: int,
    PULocationID: int
):
    try:

        features = pd.DataFrame(
            [[PULocationID, pickup_hour]],
            columns=[
                "PULocationID",
                "pickup_hour"
            ]
        )

        prediction = supply_model.predict(features)[0]

        return {
            "pickup_hour": pickup_hour,
            "PULocationID": PULocationID,
            "predicted_supply": float(prediction)
        }

    except Exception as e:
        return {"error": str(e)}
    
@app.post("/dynamic_pricing")
def dynamic_pricing(
    pickup_hour: int,
    PULocationID: int,
    base_fare: float
):
    try:

        features = pd.DataFrame(
            [[PULocationID, pickup_hour]],
            columns=[
                "PULocationID",
                "pickup_hour"
            ]
        )

        demand = demand_model.predict(features)[0]

        supply = supply_model.predict(features)[0]

        ratio = demand / max(supply, 1)

        if ratio < 1:
            multiplier = 1.0

        elif ratio < 2:
            multiplier = 1.5

        else:
            multiplier = 2.0

        final_fare = base_fare * multiplier

        return {
            "predicted_demand": round(float(demand), 2),
            "predicted_supply": round(float(supply), 2),
            "surge_multiplier": multiplier,
            "recommended_fare": round(final_fare, 2)
        }

    except Exception as e:
        return {"error": str(e)}

@app.post("/predict_cancellation")
def predict_cancellation(
    ETA: float,
    traffic_level: int,
    driver_rating: float,
    surge_multiplier: float,
    trip_distance: float,
    fare_amount: float
):

    features = pd.DataFrame(
        [[
            ETA,
            traffic_level,
            driver_rating,
            surge_multiplier,
            trip_distance,
            fare_amount
        ]],
        columns=[
            "ETA",
            "traffic_level",
            "driver_rating",
            "surge_multiplier",
            "trip_distance",
            "fare_amount"
        ]
    )

    prediction = cancellation_model.predict(features)[0]

    probability = cancellation_model.predict_proba(features)[0][1]

    return {
        "cancellation_prediction": int(prediction),
        "cancellation_probability": round(float(probability), 4),
        "risk_level": (
            "High"
            if probability > 0.7
            else "Medium"
            if probability > 0.4
            else "Low"
        )
    }

@app.post("/predict_sentiment")
def predict_sentiment(text: str):

    result = sentiment_pipeline(text)[0]

    return {
        "text": text,
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }

@app.post("/ride_matching_assistant")
def ride_matching_assistant(
    pickup_hour: int,
    PULocationID: int,
    driver_rating: float,
    cancellation_risk: float
):

    features = pd.DataFrame(
        [[PULocationID, pickup_hour]],
        columns=[
            "PULocationID",
            "pickup_hour"
        ]
    )

    demand = demand_model.predict(features)[0]
    supply = supply_model.predict(features)[0]

    score = (
        (driver_rating * 20)
        + (100 - cancellation_risk * 100)
        + (demand / max(supply, 1))
    )

    recommendation = (
        "Highly Recommended"
        if score > 150
        else "Recommended"
        if score > 100
        else "Not Recommended"
    )

    return {
        "predicted_demand": round(float(demand), 2),
        "predicted_supply": round(float(supply), 2),
        "driver_rating": driver_rating,
        "cancellation_risk": cancellation_risk,
        "match_score": round(float(score), 2),
        "recommendation": recommendation
    }