import streamlit as st
import requests

st.title("House Price Prediction")

# Input widgets for user to enter house features
crim = st.number_input("Per capita crime rate by town (crim)", value=0.1)
zn = st.number_input("Proportion of residential land zoned for large lots (zn)", value=18.0)
indus = st.number_input("Proportion of non-retail business acres per town (indus)", value=2.31)
chas = st.selectbox("Charles River dummy variable (chas)", options=[0, 1], index=0)
nox = st.number_input("Nitric oxide concentration (nox)", value=0.538)
rm = st.number_input("Average number of rooms per dwelling (rm)", value=6.0)
age = st.number_input("Proportion of owner-occupied units built before 1940 (age)", value=65.2)
dis = st.number_input("Weighted distances to employment centers (dis)", value=4.09)
rad = st.number_input("Index of accessibility to radial highways (rad)", value=1)
tax = st.number_input("Property tax rate per $10,000 (tax)", value=296.0)
ptratio = st.number_input("Pupil-teacher ratio by town (ptratio)", value=15.3)
b = st.number_input("1000(Bk - 0.63)^2 where Bk is % of Black residents (b)", value=396.9)
lstat = st.number_input("% lower status of the population (lstat)", value=4.98)

if st.button("Predict"):
    url = "http://localhost:8000/predict"
    payload = {
        "crim": crim,
        "zn": zn,
        "indus": indus,
        "chas": chas,
        "nox": nox,
        "rm": rm,
        "age": age,
        "dis": dis,
        "rad": rad,
        "tax": tax,
        "ptratio": ptratio,
        "b": b,
        "lstat": lstat
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        st.success(f"Predicted price: {response.json()['predicted_price']}")
    else:
        st.error(f"Error: {response.text}")
