import os
import joblib
from app.preprocessing import transform_raw_input

THRESHOLD = 0.60

class ChurnModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        models_dir = os.path.join(base_dir, "models")
        
        self.models = {}
        
        
        xgb_path = os.path.join(models_dir, "churn_model.pkl")
        if os.path.exists(xgb_path):
            self.models["xgboost"] = joblib.load(xgb_path)
            
        
        lr_path = os.path.join(models_dir, "churn_model_logreg.pkl")
        if os.path.exists(lr_path):
            self.models["logistic_regression"] = joblib.load(lr_path)
                
        self.scaler = joblib.load(os.path.join(models_dir, "scaler.pkl"))
        
        cols_path = os.path.join(models_dir, "feature_columns.pkl")
        if os.path.exists(cols_path):
            self.feature_columns = joblib.load(cols_path)
        else:
            self.feature_columns = [
                'gender', 'age', 'balance', 'products_number', 'active_member',
                'estimated_salary', 'country_Germany', 'balance_per_product',
                'is_zero_balance', 'age_group', 'tenure_active'
            ]
        self.is_loaded = len(self.models) > 0

    def predict(self, input_data: dict, model_type: str = "xgboost") -> dict:
        # Fallback to xgboost if specified model is not loaded
        selected_model_key = model_type if model_type in self.models else "xgboost"
        model = self.models.get(selected_model_key)
        
        if model is None:
            # Fallback to any available model
            selected_model_key = list(self.models.keys())[0]
            model = self.models[selected_model_key]

        df = transform_raw_input(input_data, self.feature_columns)
        scaled_data = self.scaler.transform(df)
        
        prob = float(model.predict_proba(scaled_data)[0][1])
        prediction = 1 if prob >= THRESHOLD else 0
        label = "High Risk" if prob >= THRESHOLD else "Low Risk"

        model_name_map = {
            "xgboost": "XGBoost Classifier",
            "logistic_regression": "Logistic Regression"
        }

        return {
            "churn_probability": round(prob, 4),
            "churn_prediction": prediction,
            "risk_label": label,
            "model_used": model_name_map.get(selected_model_key, selected_model_key.title())
        }

