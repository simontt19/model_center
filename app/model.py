import os
import lightgbm as lgb
import pandas as pd

# 自动定位到 model_center 目录下的 model.txt
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model.txt")
model = lgb.Booster(model_file=MODEL_PATH)

def predict(features: dict) -> float:
    df = pd.DataFrame([features])
    pred = model.predict(df)[0]
    return float(pred)
