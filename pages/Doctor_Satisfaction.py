import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.chart_container import chart_container
import streamlit_shadcn_ui as ui

import plotly.graph_objects as go

def create_radar_chart(data):
    categories = data['Doctor'].tolist()
    satisfaction_values = data['customer_satisfaction'].tolist()
    revisit_values = data['customer_revisit'].tolist()

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=satisfaction_values + [satisfaction_values[0]],  
        theta=categories + [categories[0]],  
        fill='toself',
        name='Customer Satisfaction',
        marker_color='#A0AEC0' 
    ))

    fig.add_trace(go.Scatterpolar(
        r=revisit_values + [revisit_values[0]], 
        theta=categories + [categories[0]],  
        fill='toself',
        name='Customer Revisit',
        marker_color='seagreen'  
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(max(satisfaction_values), max(revisit_values)) + 1]  
            )),
        showlegend=True,
        title="Customer Satisfaction and Revisit Scores by Doctor",
    )

    return fig



df = pd.read_csv('./dataset.csv')

doctor_df = df[['Doctor', 'customer_satisfaction', 'customer_revisit']]

doctor_summary = doctor_df.groupby('Doctor').agg({
    'customer_satisfaction': 'mean', 
    'customer_revisit': 'mean'       
}).reset_index()

st.title("Doctor Satisfaction Analysis")
st.write("This page provides insights into customer satisfaction and revisit rates based on individual doctors.")

st.subheader("Doctor Summary Metrics")
card_columns = st.columns(5)  

for i, row in doctor_summary.iterrows():
    with card_columns[i % 5]: 
        ui.metric_card(
            title=row['Doctor'],
            content=f"Avg Satisfaction: {row['customer_satisfaction']:.1f} / 5",
            description=f"Revisit Rate: {row['customer_revisit']}"
        )

st.subheader("Customer Satisfaction Distribution per Doctor")
satisfaction_box_fig = px.box(
    doctor_df,
    x='Doctor',
    y='customer_satisfaction',
    color='Doctor',
    color_discrete_sequence=['#38B2AC', '#2C7A7B', '#FFD166', '#FF6B6B', '#28C76F'],
    labels={'customer_satisfaction': 'Customer Satisfaction'},
)

mean_satisfaction_df = doctor_summary[['Doctor', 'customer_satisfaction']]
with chart_container(mean_satisfaction_df):
    st.plotly_chart(satisfaction_box_fig, use_container_width=True)


Doctor_revisit_df=df.groupby('Doctor')['customer_revisit'].sum().reset_index()

st.subheader("Customer Revisit Distribution per Doctor")
revisit_pie_fig = px.pie(
    Doctor_revisit_df,
    names='Doctor',
    values='customer_revisit',
    color_discrete_sequence=['#28C76F', '#2C7A7B', '#FFD166', '#FF6B6B', '#38B2AC']  # Tropical-themed colors
)

with chart_container(Doctor_revisit_df):
    st.plotly_chart(revisit_pie_fig, use_container_width=True)


radar_chart_fig = create_radar_chart(doctor_summary)
with chart_container(doctor_summary):
    st.plotly_chart(radar_chart_fig, use_container_width=True)