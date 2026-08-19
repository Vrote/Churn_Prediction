# Bank Customer Churn Prediction System

Full-stack machine learning web application for predicting bank customer churn probability based on customer demographics, tenure, account balance, number of products, and active membership status.

---

## 🏗️ Architecture Overview

- **Backend**: Python 3.10+, FastAPI, XGBoost, Scikit-learn, Pandas, Uvicorn, Python-dotenv.
- **Frontend**: React 18, Webpack 5, Babel, Custom CSS.
- **Deployment Ready**: Modular codebase with `.env` environment variables and CORS handling.

---

## 📂 Repository Structure

```text
churn_prediction/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI application endpoints
│   │   ├── model.py             # ML model loader & prediction logic
│   │   ├── preprocessing.py     # Feature scaling & encoding
│   │   └── schemas.py           # Pydantic data schemas
│   ├── models/                  # Saved XGBoost & Scaler pkl files
│   ├── .env                     # Backend environment variables
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/          # Header, CustomerForm, PredictionResult
│   │   ├── services/            # API call handler
│   │   └── App.jsx              # Main React orchestrator
│   ├── public/                  # HTML template
│   ├── .env                     # Frontend environment variables
│   └── package.json             # Node dependencies & scripts
└── README.md
```

---

## ⚡ Quick Start

### 1. Run Backend API
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Backend API docs available at `http://localhost:8000/docs`.

### 2. Run Frontend Web App
```bash
cd frontend
npm install
npm start
```
Frontend Web App available at `http://localhost:3000`.

---


## 📊 End-to-End System & Machine Learning Report

### 1. 📌 Executive Summary
Customer churn is a critical financial metric for retail banking institutions. Retaining existing customers is significantly more cost-effective than acquiring new ones. 

This project presents an **end-to-end machine learning web system** designed to predict bank customer churn probability in real time. The system combines:
- A high-performance **XGBoost Machine Learning model** (85.0% Accuracy, 87.62% ROC-AUC).
- A lightweight, asynchronous **FastAPI backend REST service**.
- A responsive, intuitive **React 18 frontend interface**.

---

### 2. 🔄 End-to-End Data Flow

```text
┌─────────────────────────┐         HTTP POST /predict         ┌─────────────────────────┐
│   React 18 Frontend     │ ─────────────────────────────────> │   FastAPI Backend API   │
│  (Collects 8 Inputs)    │ <───────────────────────────────── │  (App Listening :8000) │
└─────────────────────────┘      JSON Prediction Response      └────────────┬────────────┘
                                                                            │
                                                                 Feature Engineering &
                                                                 Scaling (8 -> 11 Features)
                                                                            │
                                                                            ▼
                                                               ┌─────────────────────────┐
                                                               │  XGBoost Classifier     │
                                                               │ (model.pkl & scaler.pkl)│
                                                               └─────────────────────────┘
```

---

### 3. 💻 Frontend Technical Specification (React 18)

* **Technology Stack**: React 18, Webpack 5, Babel, Vanilla CSS3.
* **Component Architecture**:
  - `App.jsx`: Central state manager controlling input state (`formData`), loading status (`loading`), API results (`result`), and error states (`error`).
  - `CustomerForm.jsx`: Collects 8 core customer attributes (`Gender`, `Country`, `Age`, `Tenure`, `Balance`, `Products Number`, `Active Member`, `Estimated Salary`).
  - `PredictionResult.jsx`: Dynamically renders a risk status badge (`Low Churn Risk` / `High Churn Risk`), exact probability percentage, and visual status bar.
  - `services/api.js`: Asynchronous `fetch` abstraction handling HTTP communication with the backend.

---

### 4. ⚡ Backend Technical Specification (FastAPI)

* **Technology Stack**: Python 3.10+, FastAPI, Uvicorn, Pydantic v2, Scikit-Learn, XGBoost, Pandas.
* **API Endpoints**:
  - `GET /health`: System health check verifying model loading status.
  - `POST /predict`: Receives JSON payload, executes feature engineering, scaling, model inference, and returns prediction results.
  - `GET /model/info`: Exposes model metadata and baseline metrics.
* **CORS & Middleware**: Configured with `CORSMiddleware` to safely allow cross-origin requests from the React frontend.

---

### 5. ⚙️ Feature Engineering Pipeline (8 Raw Inputs ➔ 11 Model Features)

To keep the user interface intuitive, the frontend collects **8 raw inputs**. The backend automatically executes feature engineering in `backend/app/preprocessing.py` to derive **3 additional high-signal features**:

```text
Raw Inputs (8) ────────> Feature Engineering (Backend) ────────> Model Input Vector (11)
- Gender                 1. One-Hot Encoding (country_Germany)   - gender
- Country                2. Categorical Encoding (gender)        - age
- Age                    3. balance_per_product                  - balance
- Tenure                 4. is_zero_balance                      - products_number
- Balance                5. age_group (binned 0..3)              - active_member
- Products Number        6. tenure_active (tenure * active)       - estimated_salary
- Active Member                                                  - country_Germany
- Estimated Salary                                               - balance_per_product
                                                                 - is_zero_balance
                                                                 - age_group
                                                                 - tenure_active
```

---

### 6. 📈 Machine Learning Model Evaluation

* **Algorithm**: `XGBClassifier` (Gradient Boosted Decision Trees).
* **Decision Threshold**: Tuned to **`0.35`** (rather than default `0.50`) to prioritize **Recall**—minimizing missed churn instances.

| Metric | Score | Business Impact |
|---|---|---|
| **Accuracy** | **85.0%** | High overall correctness across non-churn and churn classes |
| **ROC-AUC** | **87.62%** | Strong discrimination power between churners and non-churners |
| **Recall (Churn Class)** | **68.0%** | Successfully captures 68% of total churners for early retention intervention |
| **Precision (Churn Class)** | **61.0%** | 61% of flagged customers actually churn, ensuring efficient marketing spend |
| **F1-Score** | **64.0%** | Balanced performance metric |

---

### 7. 💡 Strategic Recommendations for Banking Operations

1. **Age-Based Retention**: Customers over 45 exhibit higher churn risk ➔ *Introduce tailored wealth preservation and retirement products.*
2. **Product Optimization**: Customers holding >2 products show elevated churn ➔ *Simplify product onboarding and bundle management.*
3. **Active Membership Engagement**: Inactive members are twice as likely to churn ➔ *Trigger automated engagement emails and loyalty rewards.*
4. **Zero-Balance Accounts**: Zero-balance accounts require low-friction maintenance features to prevent account closure.

