# app/train/random_training.py

import lightgbm as lgb
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2)

dtrain = lgb.Dataset(X_train, label=y_train)
model = lgb.train({}, dtrain, num_boost_round=10)
model.save_model("model.txt")
