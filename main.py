from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import numpy as np
import pandas as pd
import pickle
import os

app = FastAPI()

# Mount static files (for CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load the model pipeline
with open("pipe.pkl", "rb") as f:
    model = pickle.load(f)

# Teams and cities (from your model)
TEAMS = [
    "Chennai Super Kings", "Deccan Chargers", "Delhi Capitals", "Delhi Daredevils",
    "Kings XI Punjab", "Kolkata Knight Riders", "Mumbai Indians", "Rajasthan Royals",
    "Royal Challengers Bangalore", "Sunrisers Hyderabad"
]
CITIES = [
    "Abu Dhabi", "Ahmedabad", "Bangalore", "Bengaluru", "Bloemfontein", "Cape Town",
    "Centurion", "Chandigarh", "Chennai", "Cuttack", "Delhi", "Dharamsala", "Durban",
    "East London", "Hyderabad", "Indore", "Jaipur", "Johannesburg", "Kimberley",
    "Kolkata", "Mohali", "Mumbai", "Nagpur", "Port Elizabeth", "Pune", "Raipur",
    "Ranchi", "Sharjah", "Visakhapatnam"
]

@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
def index(request: Request,
          batting_team: str = Form(None),
          bowling_team: str = Form(None),
          city: str = Form(None),
          runs_left: float = Form(None),
          balls_left: float = Form(None),
          wickets: float = Form(None),
          total_runs_x: float = Form(None),
          crr: float = Form(None),
          rrr: float = Form(None)):
    result = None
    if request.method == "POST":
        input_dict = {
            "batting_team": [batting_team],
            "bowling_team": [bowling_team],
            "city": [city],
            "runs_left": [runs_left],
            "balls_left": [balls_left],
            "wickets": [wickets],
            "total_runs_x": [total_runs_x],
            "crr": [crr],
            "rrr": [rrr]
        }
        input_df = pd.DataFrame(input_dict)
        prob = model.predict_proba(input_df)[0][1]
        pred = model.predict(input_df)[0]
        result = {
            "prob": round(prob * 100, 2),
            "pred": "Win" if pred == 1 else "Lose"
        }
    return templates.TemplateResponse("index.html", {
        "request": request,
        "teams": TEAMS,
        "cities": CITIES,
        "result": result
    }) 