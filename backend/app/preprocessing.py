import pandas as pd

def transform_raw_input(data: dict, feature_columns: list) -> pd.DataFrame:
    # Extract raw inputs
    age = int(data.get("age", 30))
    tenure = int(data.get("tenure", 0))
    balance = float(data.get("balance", 0.0))
    products_number = int(data.get("products_number", 1))
    active_member = int(data.get("active_member", 1))
    estimated_salary = float(data.get("estimated_salary", 0.0))

    # Encoding gender and country
    gender = 1 if str(data.get("gender", "")).lower() == "female" else 0
    country = str(data.get("country", "")).lower()
    country_germany = 1 if country == "germany" else 0

    # Feature engineering
    balance_per_product = balance / products_number if products_number > 0 else 0.0
    is_zero_balance = 1 if balance == 0.0 else 0

    if age <= 30:
        age_group = 0
    elif age <= 45:
        age_group = 1
    elif age <= 60:
        age_group = 2
    else:
        age_group = 3

    tenure_active = tenure * active_member

    row = {
        "gender": gender,
        "age": age,
        "balance": balance,
        "products_number": products_number,
        "active_member": active_member,
        "estimated_salary": estimated_salary,
        "country_Germany": country_germany,
        "balance_per_product": balance_per_product,
        "is_zero_balance": is_zero_balance,
        "age_group": age_group,
        "tenure_active": tenure_active
    }

    df = pd.DataFrame([row])
    return df[feature_columns]
