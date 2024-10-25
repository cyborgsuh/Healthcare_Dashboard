import streamlit as st
import streamlit_themes as st_theme
st_theme.set_preset_theme('Tropical')   #Tropical, Sandy, Midnight

# Define the pages for navigation with emojis
p1 = st.Page('HOME.py', title='Main Page', icon=':material/home:')  # Home icon
p2 = st.Page('pages/BMI_Analysis.py', title='BMI Analysis', icon=':material/bar_chart:')  # Bar chart icon
p3 = st.Page('pages/Region_Analysis.py', title='Region Analysis', icon=':material/map:')  # Map icon
p4 = st.Page('pages/Age_Segmentation.py', title='Age Segmentation', icon=':material/group:')  # Group of people icon
p5 = st.Page('pages/Smoker_Analysis.py', title='Smoker Analysis', icon=':material/smoking_rooms:')  # Smoking icon
p6 = st.Page('pages/Correlation_Analysis.py', title='Correlation Analysis', icon=':material/tenancy:')  # Chart down icon
p7 = st.Page('pages/Prediction.py', title='Prediction', icon=':material/query_stats:')  # Chart up icon
p8 = st.Page('pages/Time_Series_Analysis.py', title='Time Series Analysis', icon=':material/calendar_today:')  # Calendar icon
p9=st.Page('pages/Final_Page.py', title='Final Page', icon=':material/done_outline:')  # Check icon

# Define the navigation structure


# Define the navigation structure
pg = st.navigation(
    {
        "Main Page": [p1],
        "Analysis": [p2, p3, p4, p5, p6,p8],
        "Predictions": [p7,],
        "Final Page": [p9]
    }
)
pg.run()