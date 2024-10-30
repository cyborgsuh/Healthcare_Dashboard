import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error
import plotly.express as px

df = pd.read_csv('./dataset.csv')


X = df[['age', 'bmi', 'smoker']]
y = df['charges']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    'Linear Regression': LinearRegression(),
    'Decision Tree Regressor': DecisionTreeRegressor(),
    'Random Forest Regressor': RandomForestRegressor(),
    'Support Vector Regressor': SVR()
}

results = {}

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    
    results[model_name] = {'MAE': mae, 'MSE': mse}

results_df = pd.DataFrame(results).T

st.title("ML Model Comparison for Charge Prediction")
st.subheader("Performance Metrics")

st.dataframe(results_df,use_container_width=True)

fig_mae = px.bar(results_df, x=results_df.index, y='MAE', title='Mean Absolute Error (MAE) of Different Models',
                  labels={'index': 'Models', 'MAE': 'Mean Absolute Error'},color_discrete_sequence=['seagreen'])
st.plotly_chart(fig_mae, use_container_width=True)

fig_mse = px.bar(results_df, x=results_df.index, y='MSE', title='Mean Squared Error (MSE) of Different Models',
                  labels={'index': 'Models', 'MSE': 'Mean Squared Error'},color_discrete_sequence=['seagreen'])
st.plotly_chart(fig_mse, use_container_width=True)

st.subheader("Enter Your Details for Prediction")

age = st.number_input("Age:", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI:", min_value=10.0, max_value=50.0, value=25.0,step=1.0)
smoker = st.selectbox("Smoker:", options=["no", "yes"])

smoker_numeric = 1 if smoker == "yes" else 0

input_data = np.array([[age, bmi, smoker_numeric]])

predictions = {}
for model_name, model in models.items():
    pred = model.predict(input_data)
    predictions[model_name] = pred[0]

st.subheader("Predicted Charges")
for model_name, pred in predictions.items():
    st.write(f"{model_name}: ${pred:.2f}")
