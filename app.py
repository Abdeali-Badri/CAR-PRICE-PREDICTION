import gradio as gr
import pickle
import json
import numpy as np
import os

# Load model
with open('car_price_predictor.pkl', 'rb') as f:
    model = pickle.load(f)

with open('feature_names.json', 'r') as f:
    feature_names = json.load(f)

def predict(year, present_price, kms_driven, fuel_type, seller_type, transmission, owner):
    # Prepare input
    input_data = np.array([[
        int(year),
        float(present_price),
        int(kms_driven),
        int(fuel_type),
        int(seller_type),
        int(transmission),
        int(owner)
    ]])
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    return f"💰 Predicted Selling Price: ₹{prediction:.2f} Lakhs"

# Create interface
title = "🚗 Car Price Predictor"
description = "Predict the selling price of your car based on various features"

demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(list(range(2000, 2025)), label="Manufacturing Year", value=2017),
        gr.Number(label="Present Price (in Lakhs)", value=9.85),
        gr.Number(label="Kilometers Driven", value=6900),
        gr.Dropdown([("Petrol", 0), ("Diesel", 1), ("CNG", 2)], label="Fuel Type", value=0),
        gr.Dropdown([("Dealer", 0), ("Individual", 1)], label="Seller Type", value=0),
        gr.Dropdown([("Manual", 0), ("Automatic", 1)], label="Transmission", value=0),
        gr.Slider(0, 3, step=1, label="Number of Previous Owners", value=0)
    ],
    outputs=gr.Textbox(label="Prediction"),
    title=title,
    description=description,
    examples=[
        [2017, 9.85, 6900, 0, 0, 0, 0],
        [2014, 6.87, 42450, 1, 0, 0, 0],
        [2011, 4.15, 5200, 0, 0, 0, 0]
    ],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
