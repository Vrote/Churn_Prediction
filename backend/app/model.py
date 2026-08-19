import os
import joblib
from app.preprocessing import transform_raw_input

THRESHOLD = 0.60

class ChurnModel:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        models_dir = os.path.join(base_dir, "models")
        
        self.model = joblib.load(os.path.join(models_dir, "churn_model.pkl"))
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
        self.is_loaded = True

    def predict(self, input_data: dict) -> dict:
        df = transform_raw_input(input_data, self.feature_columns)
        scaled_data = self.scaler.transform(df)
        
        prob = float(self.model.predict_proba(scaled_data)[0][1])
        prediction = 1 if prob >= THRESHOLD else 0
        label = "High Risk" if prob >= THRESHOLD else "Low Risk"

        return {
            "churn_probability": round(prob, 4),
            "churn_prediction": prediction,
            "risk_label": label
        }
