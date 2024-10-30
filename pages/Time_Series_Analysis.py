import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container

df = pd.read_csv('./dataset.csv')

df['date'] = pd.to_datetime(df['date'])

df['month'] = df['date'].dt.month_name()
df['year'] = df['date'].dt.year

monthly_summary = df.groupby(['year', 'month']).agg({
    'charges': 'mean',
    'customer_revisit': 'mean',
    'customer_satisfaction': 'mean'
}).reset_index()

monthly_summary['date_order'] = pd.to_datetime(monthly_summary['year'].astype(str) + '-' + monthly_summary['month'], format='%Y-%B')
monthly_summary = monthly_summary.sort_values(by='date_order')

charges_fig = px.line(monthly_summary, 
                      x='date_order', 
                      y='charges', 
                      labels={'charges': 'Average Charges', 'date_order': 'Month-Year'}, 
                      markers=True,
                      color_discrete_sequence=['seagreen']
                      )

revisit_fig = px.line(monthly_summary, 
                      x='date_order', 
                      y='customer_revisit', 
                      labels={'customer_revisit': 'Average Revisit Rate', 'date_order': 'Month-Year'}, 
                      markers=True,
                      color_discrete_sequence=['seagreen']
                      )

satisfaction_fig = px.line(monthly_summary,
                           x='date_order',
                           y='customer_satisfaction',
                           labels={'customer_satisfaction': 'Average Satisfaction', 'date_order': 'Month-Year'},
                           markers=True,
                           color_discrete_sequence=['seagreen']
                           )

st.title("Time-Based Analysis")

st.subheader("Average Charges Over Time")
with chart_container(monthly_summary[['month','charges']]):
    st.plotly_chart(charges_fig)

st.subheader("Average Customer Revisits Over Time")
with chart_container(monthly_summary[['month','customer_revisit']]):
    st.plotly_chart(revisit_fig)

st.subheader("Average Customer Satisfaction Over Time")
with chart_container(monthly_summary[['month','customer_satisfaction']]):
    st.plotly_chart(satisfaction_fig)
