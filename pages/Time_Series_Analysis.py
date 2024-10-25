import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container

# Load your dataset
df = pd.read_csv('./dataset.csv')

# Convert the date column to datetime (assuming there’s a 'date' column in the dataset)
df['date'] = pd.to_datetime(df['date'])

# Extract month and year for time-based analysis
df['month'] = df['date'].dt.month_name()
df['year'] = df['date'].dt.year

# Group by month and year to calculate average charges, revisits, and satisfaction
monthly_summary = df.groupby(['year', 'month']).agg({
    'charges': 'mean',
    'customer_revisit': 'mean',
    'customer_satisfaction': 'mean'
}).reset_index()

# Sort by date to ensure correct order in plots
monthly_summary['date_order'] = pd.to_datetime(monthly_summary['year'].astype(str) + '-' + monthly_summary['month'], format='%Y-%B')
monthly_summary = monthly_summary.sort_values(by='date_order')

# Line Plot: Average Charges Over Time
charges_fig = px.line(monthly_summary, 
                      x='date_order', 
                      y='charges', 
                      labels={'charges': 'Average Charges', 'date_order': 'Month-Year'}, 
                      markers=True,
                      color_discrete_sequence=['seagreen']
                      )

# Line Plot: Customer Revisits Over Time
revisit_fig = px.line(monthly_summary, 
                      x='date_order', 
                      y='customer_revisit', 
                      labels={'customer_revisit': 'Average Revisit Rate', 'date_order': 'Month-Year'}, 
                      markers=True,
                      color_discrete_sequence=['seagreen']
                      )

# Line Plot: Customer Satisfaction Over Time
satisfaction_fig = px.line(monthly_summary,
                           x='date_order',
                           y='customer_satisfaction',
                           labels={'customer_satisfaction': 'Average Satisfaction', 'date_order': 'Month-Year'},
                           markers=True,
                           color_discrete_sequence=['seagreen']
                           )

# Streamlit page content
st.title("Time-Based Analysis")

# Charges over time with chart container
st.subheader("Average Charges Over Time")
with chart_container(monthly_summary[['month','charges']]):
    st.plotly_chart(charges_fig)

# Customer revisits over time with chart container
st.subheader("Average Customer Revisits Over Time")
with chart_container(monthly_summary[['month','customer_revisit']]):
    st.plotly_chart(revisit_fig)

# Customer satisfaction over time with chart container
st.subheader("Average Customer Satisfaction Over Time")
with chart_container(monthly_summary[['month','customer_satisfaction']]):
    st.plotly_chart(satisfaction_fig)
