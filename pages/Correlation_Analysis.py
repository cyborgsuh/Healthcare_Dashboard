import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import streamlit_shadcn_ui as ui

st.title("Correlation Analysis")

df = pd.read_csv("./dataset.csv")

df_corr = df.drop(columns=['region', 'date','Doctor'])
corr = df_corr.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
corr_masked = corr.mask(mask)

annotations = np.array([['{:.2f}'.format(val) if not np.isnan(val) else '' for val in row] for row in corr_masked.values])

fig = ff.create_annotated_heatmap(
    z=corr.values,  
    x=corr_masked.columns.tolist(),  
    y=corr_masked.columns.tolist(),  
    annotation_text=annotations,  
    colorscale='greens',  
    showscale=True,  
    hoverinfo="z"
)

fig.update_traces(
    hovertemplate="<b>X: %{x}</b><br><b>Y: %{y}</b><br><b>Correlation: %{z:.2f}</b><extra></extra>"
)

fig.update_layout(
    xaxis=dict(tickangle=45),
    yaxis=dict(tickangle=0),
    width=800, height=800,
)

st.subheader("Correlation Heatmap")
st.plotly_chart(fig)

corr_pairs = corr.unstack().dropna()  
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]  

highest_positive = corr_pairs[corr_pairs > 0].idxmax()
highest_positive_value = corr_pairs.max()

highest_negative = corr_pairs[corr_pairs < 0].idxmin()
highest_negative_value = corr_pairs.min()

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
