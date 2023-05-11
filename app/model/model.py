from catboost import CatBoostRegressor
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

model = CatBoostRegressor()
model.load_model(f'{BASE_DIR}/cat_model')
