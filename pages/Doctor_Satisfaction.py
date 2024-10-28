import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container
import streamlit_shadcn_ui as ui

# Load the dataset
df = pd.read_csv('./dataset.csv')

# Filter relevant data
doctor_df = df[['Doctor', 'customer_satisfaction', 'customer_revisit']]

# Calculate aggregated metrics for each doctor
doctor_summary = doctor_df.groupby('Doctor').agg({
    'customer_satisfaction': 'mean',   # Average customer satisfaction per doctor
    'customer_revisit': 'sum'          # Total revisits per doctor
}).reset_index()

# Set up the page
st.title("Doctor Satisfaction Analysis")
st.write("This page provides insights into customer satisfaction and revisit rates based on individual doctors.")

# Display Metric Cards in a Grid
st.subheader("Doctor Summary Metrics")
card_columns = st.columns(5)  # Five columns for up to five doctors

for i, row in doctor_summary.iterrows():
    with card_columns[i % 5]:  # Use modulo to wrap cards in a new row after 5
        ui.metric_card(
            title=row['Doctor'],
            content=f"Avg Satisfaction: {row['customer_satisfaction']:.1f} / 5",
            description=f"Revisit Rate: {row['customer_revisit']}"
        )

# Visualization: Customer Satisfaction per Doctor (Box Plot)
st.subheader("Customer Satisfaction Distribution per Doctor")
satisfaction_box_fig = px.box(
    doctor_df,
    x='Doctor',
    y='customer_satisfaction',
    color='Doctor',
    color_discrete_sequence=['#38B2AC', '#2C7A7B', '#FFD166', '#FF6B6B', '#28C76F'],
    labels={'customer_satisfaction': 'Customer Satisfaction'},
)

# Show the box plot in a chart container
mean_satisfaction_df = doctor_summary[['Doctor', 'customer_satisfaction']]
with chart_container(mean_satisfaction_df):
    st.plotly_chart(satisfaction_box_fig, use_container_width=True)


# Visualization: Customer Revisit Distribution per Doctor (Pie Chart)
st.subheader("Customer Revisit Distribution per Doctor")
revisit_pie_fig = px.pie(
    doctor_summary,
    names='Doctor',
    values='customer_revisit',
    color_discrete_sequence=['#28C76F', '#2C7A7B', '#FFD166', '#FF6B6B', '#38B2AC']  # Tropical-themed colors
)

# Show the pie chart in a chart container
with chart_container(doctor_summary[['Doctor', 'customer_revisit']]):
    st.plotly_chart(revisit_pie_fig, use_container_width=True)
