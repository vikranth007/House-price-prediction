# 🏠 House Price Prediction using Machine Learning

This project focuses on predicting house prices using machine learning models based on features such as number of bedrooms, area, location, etc.

## 📌 Project Overview

In the real estate market, accurate house price prediction is essential for buyers, sellers, and investors. This project aims to build a regression model that can predict the price of a house given several input features.

## 💡 Features Used

- Area (square feet)
- Number of bedrooms
- Number of bathrooms
- Location
- Parking space
- Age of the house
- Furnishing status (furnished/unfurnished/semi-furnished)

## 🧠 Models Used

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn (for visualization)
- Jupyter Notebook

## 📁 Project Structure


  House-Price-Prediction/
  │
  ├── data/
  │ └── housing.csv # Dataset file
  ├── notebooks/
  │ └── EDA_and_Modeling.ipynb # Jupyter Notebook for analysis and model building
  ├── models/
  │ └── model.pkl # Trained model (pickle file)
  ├── app/
  │ └── app.py # (Optional) Flask or Streamlit app
  ├── README.md
  └── requirements.txt # Python dependencies



## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/house-price-prediction.git
   cd house-price-prediction
2. **requirements:**
   pip install -r requirements.txt

3. **Run the notebook**
  Open EDA_and_Modeling.ipynb in Jupyter Notebook or VS Code and run the cells.
  using the uvicorn to run the main.py
    #uvicorn main:app --reload
   
4. **Run the app**
  **streamlit** run app/app.py # using the terminal

## 📊 Results
  Best Model: Random Forest Regressor
  
  R² Score: 0.87
  
  RMSE: ₹4.2 Lakhs

## 📌 Future Work
  Add more feature engineering
  
  Use XGBoost or CatBoost
  
  Hyperparameter tuning
  
  Deploy the model as a web app

## 📚 Dataset
The dataset was sourced from Kaggle or other real estate portals.

