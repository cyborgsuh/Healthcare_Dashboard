import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container

# Load the dataset (ensure correct path)
df = pd.read_csv('./dataset.csv')

# Age Segmentation Logic
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=[18, 25, 35, 45, 55, 65, 120], labels=age_groups)

# Aggregating charges, satisfaction, revisits, and smoker count by age group
age_group_summary = df.groupby('age_group').agg({
    'charges': 'mean',
    'customer_satisfaction': 'mean',
    'customer_revisit': 'mean',
    'smoker': 'sum'  # Count of smokers (assuming 1 for smokers and 0 for non-smokers)
}).reset_index()

# Renaming the smoker column for clarity
age_group_summary.rename(columns={'smoker': 'smoker_count'}, inplace=True)

# Plotting charges by age group
age_charge = px.bar(age_group_summary, x='age_group', y='charges', color_discrete_sequence=['seagreen'])
age_smoker = px.bar(age_group_summary, x='age_group', y='smoker_count', color_discrete_sequence=['seagreen'])

# Streamlit page content
st.title("Age-based Segmentation")

# Charges chart with chart container
st.subheader("Average Charges by Age Group")
with chart_container(age_group_summary[['age_group', 'charges']]):
    st.plotly_chart(age_charge, theme='streamlit')

# Smoker count chart with chart container
st.subheader('Smoker Count in each Age Group')
with chart_container(age_group_summary[['age_group', 'smoker_count']]):
    st.plotly_chart(age_smoker, theme='streamlit')
    
    
st.subheader('Average Satisfaction and Revisit Rate by Age Group')
st.dataframe(age_group_summary[['age_group', 'customer_satisfaction', 'customer_revisit']], use_container_width=True)