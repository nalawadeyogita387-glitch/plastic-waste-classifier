from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ClassificationRequest(BaseModel):
    image_name: str
    category: str


@app.get("/")
def home():
    return {"message": "Plastic Waste Classifier Backend is Running"}


@app.post("/classify")
def classify(request: ClassificationRequest):
    return {
        "image": request.image_name,
        "category": request.category,
        "status": "Classification completed"
    }