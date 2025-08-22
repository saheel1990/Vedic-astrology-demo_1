from fastapi import FastAPI
from pydantic import BaseModel
from app.astrology import sample_chart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Vedic Astrology Blueprint API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChartRequest(BaseModel):
    name: str
    birth_iso: str  # e.g. 1990-04-20T05:25:00
    lat: float = 0.0
    lon: float = 0.0

@app.get("/")
def hello():
    return {"message":"Vedic Astrology Blueprint API - demo"}

@app.post("/chart")
def chart(req: ChartRequest):
    return sample_chart(req.name, req.birth_iso, req.lat, req.lon)
