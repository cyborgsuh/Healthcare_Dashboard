import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit_shadcn_ui as ui

# Load dataset
df = pd.read_csv('./dataset.csv')

# Header for the dashboard
st.title("Regional Analysis Dashboard")

# Region selection
regions = df['region'].unique().tolist()
regions = ['All Regions'] + regions  # Add option for all regions
selected_region = st.selectbox("Select a Region", regions)

# Filter data for the selected region
if selected_region == 'All Regions':
    df_region = df
else:
    df_region = df[df['region'] == selected_region]

# Compute region-specific metrics
region_total_charges = df_region['charges'].sum()
region_avg_bmi = df_region['bmi'].mean()
region_smoker_count = df_region[df_region['smoker'] == 1].shape[0]
region_total_customers = df_region.shape[0]
region_smoker_ratio = (region_smoker_count / region_total_customers) * 100 if region_total_customers > 0 else 0


st.header(f"Regional Analysis for {selected_region}")

# Display region-specific cards
cols = st.columns(3)
with cols[0]:
    ui.metric_card(
        title=f"Total Charges",
        content=f"${region_total_charges / 1e6:.1f}M",  # Show in millions
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

# Bar Chart: Average Charges in Selected Region
st.subheader(f"Average Charges in {selected_region} vs Other Regions")
# Calculate average charges for all regions and the selected region
df_avg_charges = df.groupby('region')['charges'].mean().reset_index()
if selected_region != 'All Regions':
    selected_region_avg = df_avg_charges[df_avg_charges['region'] == selected_region]['charges'].values[0]
global_avg = df['charges'].mean()

# Create the bar chart with comparison to all regions and highlight the selected region
bar_chart = px.bar(df_avg_charges,
                   x='region',
                   y='charges',
                   labels={'charges': 'Average Charges ($)'},
                   color_discrete_sequence=['#A0AEC0']  # Default color for other regions
                   )

# Highlight the selected region by changing its color
bar_chart.update_traces(marker=dict(color=['seagreen' if region == selected_region else '#A0AEC0' 
                                           for region in df_avg_charges['region']]))

# Add a target line showing the global average charges
bar_chart.add_shape(type="line",
                    line=dict(dash="dash", color="red"),
                    x0=-0.5, x1=len(df_avg_charges)-0.5,
                    y0=global_avg, y1=global_avg)

# Add an annotation for the global average line
bar_chart.add_annotation(x=len(df_avg_charges)-0.5, y=global_avg, text=f"Avg Charges: ${global_avg:,.2f}", showarrow=False, font=dict(color="red"))

# Annotate the selected region bar with its actual value
bar_chart.update_traces(texttemplate='%{y:.2f}', textposition='outside')

# Display the chart
st.plotly_chart(bar_chart, use_container_width=True)

# Pie Chart: Smokers Distribution in Selected Region
st.subheader(f"Smoker Distribution in {selected_region}")
# Tropical Fruit Palette
df_smoker_count = df_region['smoker'].value_counts().reset_index()
df_smoker_count.columns = ['smoker', 'count']

# Create the pie chart using the count of smokers
pie_chart = px.pie(df_smoker_count, names='smoker', values='count', 
                   color_discrete_sequence=['seagreen', '#A0AEC0'])

# Display the pie chart in Streamlit
st.plotly_chart(pie_chart, use_container_width=True)

# Box Plot: BMI Distribution in Selected Region
st.subheader(f"BMI Distribution in {selected_region}")
box_chart = px.box(df_region, x='region', y='bmi', color='region',
                   color_discrete_sequence=['seagreen','#A0AEC0'])
st.plotly_chart(box_chart, use_container_width=True)
