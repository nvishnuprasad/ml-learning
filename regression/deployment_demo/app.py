from fastapi import FastAPI
import joblib
import pandas as pd
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Rental Price Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


ARTIFACTS_DIR = Path("./../artifacts")


def load_latest_model():
    """
    Picks the most recently modified rent_model_pipeline_*.joblib
    from the artifacts folder.
    """
    model_files = list(ARTIFACTS_DIR.glob("rent_model_pipeline_*.joblib"))
    if not model_files:
        raise FileNotFoundError("No model files found in artifacts folder")

    latest_model = max(model_files, key=lambda f: f.stat().st_mtime)
    return joblib.load(latest_model)


# Load model at startup
model = load_latest_model()


@app.post("/predict")
def predict(payload: dict):
    """
    Expects a single rental record as JSON.
    """
    df = pd.DataFrame([payload])
    prediction = model.predict(df)[0]

    return {
        "predicted_rent": f"₹{int(prediction):,}"
    }
