import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container

# Load the dataset
df = pd.read_csv('./dataset.csv')

# Create BMI categories
bmi_categories = ['Underweight', 'Normal', 'Overweight', 'Obese']
df['bmi_category'] = pd.cut(df['bmi'], bins=[0, 18.5, 24.9, 29.9, 100], labels=bmi_categories)

# Aggregating charges, satisfaction, and smoker count by BMI category
bmi_summary = df.groupby('bmi_category').agg({
    'charges': 'mean',
    'customer_satisfaction': 'mean',
    'smoker': 'sum'  # Assuming smoker is binary (1 for smoker, 0 for non-smoker)
}).reset_index()

# Plotting average charges by BMI category
average_charges_bmi = px.bar(bmi_summary, x='bmi_category', y='charges', color_discrete_sequence=['seagreen'])

# Plotting smoker counts by BMI category
smoker_counts_per_bmi = px.bar(bmi_summary, x='bmi_category', y='smoker', color_discrete_sequence=['seagreen'])

# Streamlit page content
st.title("BMI-based Segmentation")

# Display average charges by BMI category with chart container
st.subheader("Average Charges by BMI Category")
with chart_container(bmi_summary[['bmi_category','charges']]):
    st.plotly_chart(average_charges_bmi)

# Display smoker counts by BMI category with chart container
st.subheader("Smoker Counts by BMI Category")
with chart_container(bmi_summary[['bmi_category','smoker']]):
    st.plotly_chart(smoker_counts_per_bmi)
