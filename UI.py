import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import os


st.title("Retail Store Demand Forecasting")
st.markdown("Forecast future demand using historical sales data with Facebook Prophet.")

# Check if file exists
if os.path.exists("retail_store_inventory.csv"):
    st.info("Using default dataset: `retail_store_inventory.csv`")
    df = pd.read_csv("retail_store_inventory.csv")
else:
    st.error("File `retail_store_inventory.csv` not found in the directory.")
    st.stop()

# Preprocessing
df['Date'] = pd.to_datetime(df['Date'])
df_grouped = df.groupby('Date')['Units Sold'].sum().reset_index()
df_grouped.columns = ['ds', 'y']

# Forecast duration selector
periods = st.slider("Select forecast horizon (days)", min_value=7, max_value=90, step=7, value=30)

# Train the Prophet model
model = Prophet()
model.fit(df_grouped)

# Make future predictions
future = model.make_future_dataframe(periods=periods)
forecast = model.predict(future)

# Plot the forecast
st.subheader("Forecast Plot")
fig1 = model.plot(forecast)
st.pyplot(fig1)

# Evaluation
merged = pd.merge(forecast[['ds', 'yhat']], df_grouped, how='inner', on='ds')
mae = mean_absolute_error(merged['y'], merged['yhat'])
rmse = np.sqrt(mean_squared_error(merged['y'], merged['yhat']))

st.subheader("Model Evaluation")
st.metric("MAE", f"{mae:.2f}")
st.metric("RMSE", f"{rmse:.2f}")

# Forecast Data Table
st.subheader("Forecast Data")
st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods))
