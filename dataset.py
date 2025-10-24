from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib  # or use pickle
import numpy as np
import pandas as pd

# Load model
model = joblib.load("logistic_model.pkl")

# Init app
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Serve home page
@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Predict endpoint
@app.post("/predict")
async def predict(
    temperature: float = Form(...),
    ambient_temperature: float = Form(...),
    sample: str = Form(...)
):
    print(temperature)
    temp=[temperature],
    Ambient=[ambient_temperature]
    
    new_data={
    'temp':[temperature],
    'Ambient':[ambient_temperature],
    'Sample_0.35 Nominal':[False],
    'Sample_0.4 Nominal': [False],
    'Sample_0.4 Wc+10% Silica':[False],
    'Sample_0.45 Nominal':[False],
    'Sample_0.4Wc+ 10% GGBS':[False],
    'Sample_0.4Wc+10% Fly Ash':[False]
    }
    print(new_data)
    col=sample
    if col in list(new_data.keys()):
        new_data[col]=[True]
    
    df_to_pricict=pd.DataFrame(new_data)

    prediction = model.predict(df_to_pricict)
    print(prediction[0])
    if prediction[0]==1:
        pred = 'Tending to strong...'
    else:
        pred='Tending to weak....'
    return {"prediction": pred}
