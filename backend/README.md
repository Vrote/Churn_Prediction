# Bank Customer Churn Prediction - Backend API

FastAPI backend application for serving customer churn risk predictions using an XGBoost Machine Learning model.

---

## 📌 Features
- **FastAPI Endpoints**: High-performance REST API with automated OpenAPI interactive documentation (`/docs`).
- **XGBoost ML Pipeline**: Loads pre-trained scaler (`scaler.pkl`) and model (`churn_model.pkl`) once on startup.
- **Environment Configuration**: Configured with `python-dotenv` to manage `HOST`, `PORT`, and `CORS_ORIGINS`.
- **Health Checks**: Endpoint (`/health`) to monitor model loading status.

---

## 🛠️ Tech Stack
- **Framework**: FastAPI + Uvicorn
- **ML Libraries**: XGBoost, Scikit-learn, Joblib, Pandas, NumPy
- **Validation**: Pydantic v2

---

## 🚀 Setup & Running Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
Check `.env` file (or copy from `.env.example`):
```env
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 3. Start Server
```bash
uvicorn app.main:app --reload --port 8000
```
Interactive Swagger API documentation will be available at `http://localhost:8000/docs`.

---

## 📡 API Endpoints

### 1. GET `/health`
Returns API operational status and confirms whether the model is loaded.
```bash
curl http://localhost:8000/health
```

### 2. POST `/predict`
Predicts churn probability for a given customer profile.
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "gender": "Female",
           "country": "Germany",
           "age": 42,
           "tenure": 2,
           "balance": 83807.86,
           "products_number": 3,
           "active_member": 0,
           "estimated_salary": 112542.58
         }'
```

**Response**:
```json
{
  "churn_probability": 0.9185,
  "churn_prediction": 1,
  "risk_label": "High Risk"
}
```

### 3. GET `/model/info`
Returns model type, decision threshold, and evaluation metrics.
```bash
curl http://localhost:8000/model/info
```

---

## 📂 Project Structure
```text
backend/
├── app/
│   ├── main.py          # FastAPI application & CORS configuration
│   ├── model.py         # ChurnModel loader class & predict method
│   ├── preprocessing.py # Preprocessing & feature scaling pipelines
│   └── schemas.py       # Pydantic input/output schemas
├── models/              # Pre-trained .pkl artifacts
├── .env                 # Environment variables
├── .env.example         # Sample environment template
└── requirements.txt     # Python package dependencies
```
