import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
df = pd.read_csv('./dataset.csv')

# Group by smoker status for average charges and satisfaction
smoker_summary = df.groupby('smoker').agg({
    'charges': 'mean',
    'customer_satisfaction': 'mean'
}).reset_index()

#Replacing numbers to words for better understanding
smoker_summary.replace({1: "Yes", 0: "No"}, inplace=True)
df['smoker']=df['smoker'].replace({1: "Yes", 0: "No"})

# Plotting average charges by smoker status
charges_fig = px.bar(
    smoker_summary,
    x='smoker',
    y='charges',
    title='Average Charges: Smokers vs Non-Smokers',
    color='smoker',  
    color_continuous_scale='greens',
    labels={'charges': 'Average Charges', 'smoker': 'Smoker Status'},
    color_discrete_sequence=['#A0AEC0','seagreen'],
    
)
# Plotting average satisfaction by smoker status
satisfaction_fig = px.bar(smoker_summary, 
    x='smoker', 
    y='customer_satisfaction', 
    title='Customer Satisfaction: Smokers vs Non-Smokers', 
    color='smoker',
    color_continuous_scale='greens',
    labels={'customer_satisfaction': 'Average Satisfaction', 'smoker': 'Smoker Status'},
    color_discrete_sequence=['#A0AEC0','seagreen'])

# Box Plot: Distribution of Charges for Smokers vs Non-Smokers
box_fig = px.box(df, 
    x='smoker', 
    y='charges', 
    title='Charges Distribution: Smokers vs Non-Smokers', 
    color='smoker',
    labels={'charges': 'Charges', 'smoker': 'Smoker Status'},
    color_discrete_sequence=['seagreen','#A0AEC0'],
    )

# Streamlit page content
st.title("Smoker vs Non-Smoker Analysis")

st.subheader("Average Charges Comparison")
st.plotly_chart(charges_fig)

st.subheader("Customer Satisfaction Comparison")
st.plotly_chart(satisfaction_fig)

st.subheader("Distribution of Charges")
st.plotly_chart(box_fig)

# Show summary data as a table
st.subheader("Summary Data")
st.dataframe(smoker_summary)
