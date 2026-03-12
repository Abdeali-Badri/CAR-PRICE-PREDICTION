🚗 Car Price Prediction
A machine learning app that predicts the selling price of a used car based on its features — built with scikit-learn and deployed via a Gradio interface.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-UI-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML%20Model-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

# Overview :-
This project predicts the resale price of a used car using a trained regression model. The user inputs car details like year, fuel type, transmission, and kilometers driven, and the model returns an estimated selling price instantly through a Gradio web UI.

# Key Features :-

🔮 Instant price prediction from car details
🧠 Trained on real car sales data (car data.csv)
🌐 Gradio interface — interactive and easy to use
📦 Feature names stored in JSON for clean inference pipeline


# Tech Stack :-
ComponentTechnologyML Modelscikit-learnUI FrameworkGradioDatasetCSV (car data)LanguagePython 3.x

# Project Structure :-
```
CAR-PRICE-PREDICTION/
│
├── car_price_prediction.py   # Model training script
├── app.py                    # Gradio app — loads model and runs UI
├── car data.csv              # Dataset used for training
├── feature_names.json        # Saved feature names for inference
└── README.md
```

# Getting Started :-
```bash
# Clone the repository
git clone https://github.com/Abdeali-Badri/CAR-PRICE-PREDICTION.git
cd CAR-PRICE-PREDICTION
```

# Install dependencies :-
```bash
pip install -r requirements.txt
```

# Run the app :-
```bash
python app.py
```

# Inputs Used for Prediction :-

1) Car Name / Model
2) Year of manufacture
3) Kilometers driven
4) Fuel type (Petrol / Diesel / CNG)
5) Seller type
6) Transmission (Manual / Automatic)
7) Number of previous owners

## Author

**Abdeali Badri**

[![GitHub](https://img.shields.io/badge/GitHub-Abdeali--Badri-181717?style=for-the-badge&logo=github)](https://github.com/Abdeali-Badri)
