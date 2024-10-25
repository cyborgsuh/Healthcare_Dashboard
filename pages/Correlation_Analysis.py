import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import streamlit_shadcn_ui as ui

st.title("Correlation Analysis")

# Load the dataset
df = pd.read_csv("./dataset.csv")

# Drop non-numeric columns for correlation analysis
df_corr = df.drop(columns=['region', 'date'])
corr = df_corr.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
corr_masked = corr.mask(mask)

# Create annotations formatted to 2 decimal places
annotations = np.array([['{:.2f}'.format(val) if not np.isnan(val) else '' for val in row] for row in corr_masked.values])

# Create a Plotly heatmap with hover information for x, y, and correlation values
fig = ff.create_annotated_heatmap(
    z=corr.values,  # Correlation values
    x=corr_masked.columns.tolist(),  # X-axis labels
    y=corr_masked.columns.tolist(),  # Y-axis labels
    annotation_text=annotations,  # Add formatted annotations
    colorscale='greens',  # Color scale (similar to coolwarm)
    showscale=True,  # Show color scale
    hoverinfo="z"  # Hover info for correlation value (z) and axes
)

# Customize hovertemplate to include x and y labels, and format the correlation value
fig.update_traces(
    hovertemplate="<b>X: %{x}</b><br><b>Y: %{y}</b><br><b>Correlation: %{z:.2f}</b><extra></extra>"
)

# Update layout for better readability and aesthetics
fig.update_layout(
    xaxis=dict(tickangle=45),
    yaxis=dict(tickangle=0),
    width=600, height=600,
)

# Show the figure
st.subheader("Correlation Heatmap")
st.plotly_chart(fig)

# Find highest positive and negative correlations excluding self-correlation
corr_pairs = corr.unstack().dropna()  # Flatten the correlation matrix
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]  # Exclude self-correlations

# Get the highest positive correlation and the corresponding feature names
highest_positive = corr_pairs[corr_pairs > 0].idxmax()
highest_positive_value = corr_pairs.max()

# Get the highest negative correlation and the corresponding feature names
highest_negative = corr_pairs[corr_pairs < 0].idxmin()
highest_negative_value = corr_pairs.min()

# Display cards for highest positive and negative correlations
cols = st.columns(2)

with cols[0]:
    ui.metric_card(
        title=f"Highest Positive Correlation: {highest_positive[0]} & {highest_positive[1]}",
        content=f"{highest_positive_value:.2f}",
        description="Features with the highest positive correlation"
    )

with cols[1]:
    ui.metric_card(
        title=f"Highest Negative Correlation: {highest_negative[0]} & {highest_negative[1]}",
        content=f"{highest_negative_value:.2f}",
        description="Features with the highest negative correlation"
    )
