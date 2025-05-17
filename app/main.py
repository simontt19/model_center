from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict

app = FastAPI()

class PredictRequest(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float


@app.post("/predict")
def predict_api(req: PredictRequest):
    result = predict(req.dict())
    return {"prediction": result}
