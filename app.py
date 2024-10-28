import streamlit as st
import streamlit_themes as st_theme
st_theme.set_preset_theme('Tropical')   #Tropical, Sandy, Midnight
#setting wide layout
st.set_page_config(layout="wide")

p1 = st.Page('HOME.py', title='Main Page', icon=':material/home:')  
p2 = st.Page('pages/BMI_Analysis.py', title='BMI Analysis', icon=':material/bar_chart:')  
p3 = st.Page('pages/Region_Analysis.py', title='Region Analysis', icon=':material/map:')  
p4 = st.Page('pages/Age_Segmentation.py', title='Age Segmentation', icon=':material/group:')  
p5 = st.Page('pages/Smoker_Analysis.py', title='Smoker Analysis', icon=':material/smoking_rooms:')  
p6 = st.Page('pages/Correlation_Analysis.py', title='Correlation Analysis', icon=':material/tenancy:')
p7 = st.Page('pages/Prediction.py', title='Prediction', icon=':material/query_stats:')  
p8 = st.Page('pages/Time_Series_Analysis.py', title='Time Series Analysis', icon=':material/calendar_today:') 
p9=st.Page('pages/Final_Page.py', title='Final Page', icon=':material/done_outline:')  
p10=st.Page('pages/Doctor_Satisfaction.py', title='Doctor Satisfaction', icon=':material/account_circle:')
pg = st.navigation(
    {
        "Main Page": [p1],
        "Analysis": [p2, p3, p4, p5, p6,p8,p10],
        "Predictions": [p7,],
        "Final Page": [p9]
    }
)
pg.run()