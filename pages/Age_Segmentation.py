import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.chart_container import chart_container

# Loading DS
df = pd.read_csv('./dataset.csv')

# Age Segmentation Logic
age_groups = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
df['age_group'] = pd.cut(df['age'], bins=[18, 25, 35, 45, 55, 65, 120], labels=age_groups)

age_group_summary = df.groupby('age_group').agg({
    'charges': 'mean',
    'customer_satisfaction': 'mean',
    'customer_revisit': 'mean',
    'smoker': 'sum'  # 1 for smokers and 0 for non smokers
}).reset_index()

age_group_summary.rename(columns={'smoker': 'smoker_count'}, inplace=True)

age_charge = px.bar(age_group_summary, x='age_group', y='charges', color_discrete_sequence=['seagreen'])
age_smoker = px.bar(age_group_summary, x='age_group', y='smoker_count', color_discrete_sequence=['seagreen'])

st.title("Age-based Segmentation")

st.subheader("Average Charges by Age Group")
with chart_container(age_group_summary[['age_group', 'charges']]):
    st.plotly_chart(age_charge, theme='streamlit')

st.subheader('Smoker Count in each Age Group')
with chart_container(age_group_summary[['age_group', 'smoker_count']]):
    st.plotly_chart(age_smoker, theme='streamlit')
    
    
st.subheader('Average Satisfaction and Revisit Rate by Age Group')
st.dataframe(age_group_summary[['age_group', 'customer_satisfaction', 'customer_revisit']], use_container_width=True)