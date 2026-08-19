import os
import logging
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CustomerInput, PredictionResponse
from app.model import ChurnModel, THRESHOLD

# Load environment variables from .env
load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
CORS_ORIGINS = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "*").split(",")]

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

churn_model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global churn_model
    # Load model once at startup for fast predictions
    churn_model = ChurnModel()
    logger.info("Model loaded successfully.")
    yield

app = FastAPI(title="Churn Prediction API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": churn_model is not None and churn_model.is_loaded}

@app.post("/predict", response_model=PredictionResponse)
def predict(data: CustomerInput):
    if not churn_model or not churn_model.is_loaded:
        raise HTTPException(status_code=503, detail="Model not loaded")

    raw_dict = data.model_dump()
    result = churn_model.predict(raw_dict)
    logger.info(f"Prediction result: {result}")

    return result

@app.get("/model/info")
def model_info():
    num_features = len(churn_model.feature_columns) if churn_model else 11
    return {
        "model_type": "XGBClassifier",
        "number_of_features": num_features,
        "decision_threshold": THRESHOLD,
        "metrics": {
            "accuracy": 0.85,
            "churn_precision": 0.61,
            "churn_recall": 0.68,
            "churn_f1": 0.64,
            "roc_auc": 0.8762
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
