import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_shadcn_ui as ui

df = pd.read_csv('./dataset.csv')

st.title("Regional Analysis Dashboard")

regions = df['region'].unique().tolist()
regions = ['All Regions'] + regions  
selected_region = st.selectbox("Select a Region", regions)

if selected_region == 'All Regions':
    df_region = df
else:
    df_region = df[df['region'] == selected_region]

region_total_charges = df_region['charges'].sum()
region_avg_bmi = df_region['bmi'].mean()
region_smoker_count = df_region[df_region['smoker'] == 1].shape[0]
region_total_customers = df_region.shape[0]
region_smoker_ratio = (region_smoker_count / region_total_customers) * 100 if region_total_customers > 0 else 0


st.header(f"Regional Analysis for {selected_region}")

cols = st.columns(3)
with cols[0]:
    ui.metric_card(
        title=f"Total Charges",
        content=f"${region_total_charges / 1e6:.1f}M",  
    )

with cols[1]:
    ui.metric_card(
        title=f"Average BMI",
        content=f"{region_avg_bmi:.2f}",
    )

with cols[2]:
    ui.metric_card(
        title=f"Smoker Proportion",
        content=f"{region_smoker_ratio:.1f}%",
    )

st.subheader(f"Average Charges in {selected_region} vs Other Regions")
df_avg_charges = df.groupby('region')['charges'].mean().reset_index()


global_avg = df['charges'].mean()

bar_chart = px.bar(df_avg_charges,
            x='region',
            y='charges',
            labels={'charges': 'Average Charges ($)'},
            color_discrete_sequence=['#A0AEC0']  
            )

bar_chart.update_traces(marker=dict(color=['seagreen' if region == selected_region else '#A0AEC0' 
                        for region in df_avg_charges['region']]))

bar_chart.add_shape(type="line",
                    line=dict(dash="dash", color="red"),
                    x0=-0.5, x1=len(df_avg_charges)-0.5,
                    y0=global_avg, y1=global_avg)

bar_chart.add_annotation(x=len(df_avg_charges)-0.5, y=global_avg, text=f"Avg Charges: ${global_avg:,.2f}", showarrow=False, font=dict(color="red"))

bar_chart.update_traces(texttemplate='%{y:.2f}', textposition='outside')

st.plotly_chart(bar_chart, use_container_width=True)

st.subheader(f"Smoker Distribution in {selected_region}")
df_smoker_count = df_region['smoker'].value_counts().reset_index()
df_smoker_count.columns = ['smoker', 'count']

pie_chart = px.pie(df_smoker_count, names='smoker', values='count', 
                color_discrete_sequence=['seagreen', '#A0AEC0'])

st.plotly_chart(pie_chart, use_container_width=True)

st.subheader(f"BMI Distribution in {selected_region}")
box_chart = px.box(df_region, x='region', y='bmi', color='region',
                color_discrete_sequence=['seagreen','#A0AEC0'])
st.plotly_chart(box_chart, use_container_width=True)
