import os
import sys
import logging
from pathlib import Path
from contextlib import asynccontextmanager

# Add backend root directory to sys.path so app module is discoverable
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import CustomerInput, PredictionResponse
from app.model import ChurnModel, THRESHOLD

# Load environment variables from .env
load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
CORS_ORIGINS = [origin.strip() for origin in os.getenv("CORS_ORIGINS", "*").split(",") if origin.strip()]
allow_all_origins = "*" in CORS_ORIGINS or not CORS_ORIGINS

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
    allow_origins=["*"] if allow_all_origins else CORS_ORIGINS,
    allow_credentials=not allow_all_origins,
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
    model_type = getattr(data, "model_type", "xgboost")
    result = churn_model.predict(raw_dict, model_type=model_type)
    logger.info(f"Prediction result: {result}")

    return result

@app.get("/model/info")
def model_info():
    num_features = len(churn_model.feature_columns) if churn_model else 11
    loaded_models = list(churn_model.models.keys()) if churn_model else []
    return {
        "available_models": loaded_models,
        "number_of_features": num_features,
        "decision_threshold": THRESHOLD,
        "models_info": {
            "xgboost": {
                "name": "XGBoost Classifier",
                "status": "loaded" if "xgboost" in loaded_models else "not loaded",
                "metrics": {
                    "accuracy": 0.85,
                    "precision": 0.61,
                    "recall": 0.68,
                    "f1": 0.64,
                    "roc_auc": 0.8762
                }
            },
            "logistic_regression": {
                "name": "Logistic Regression",
                "status": "loaded" if "logistic_regression" in loaded_models else "not loaded",
                "metrics": {
                    "accuracy": 0.7023,
                    "precision": 0.3743,
                    "recall": 0.6858,
                    "f1": 0.4842,
                    "roc_auc": 0.7564
                }
            }
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
