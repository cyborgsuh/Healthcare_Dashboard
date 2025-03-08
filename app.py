import streamlit as st
import streamlit_themes as st_theme
st_theme.set_preset_theme('Tropical')#Tropical,Sandy,Midnight
st.set_page_config(layout="wide")

p1=st.Page('HOME.py',title='MainPage',icon=':material/home:')
p2=st.Page('pages/BMI_Analysis.py',title='BMIAnalysis',icon=':material/bar_chart:')
p3=st.Page('pages/Region_Analysis.py',title='RegionAnalysis',icon=':material/map:')
p4=st.Page('pages/Age_Segmentation.py',title='AgeSegmentation',icon=':material/group:')
p5=st.Page('pages/Smoker_Analysis.py',title='SmokerAnalysis',icon=':material/smoking_rooms:')
p6=st.Page('pages/Correlation_Analysis.py',title='CorrelationAnalysis',icon=':material/tenancy:')
p7=st.Page('pages/Prediction.py',title='Prediction',icon=':material/query_stats:')
p8=st.Page('pages/Time_Series_Analysis.py',title='TimeSeriesAnalysis',icon=':material/calendar_today:')
p9=st.Page('pages/Final_Page.py',title='FinalPage',icon=':material/done_outline:')
p10=st.Page('pages/Doctor_Satisfaction.py',title='DoctorSatisfaction',icon=':material/account_circle:')

pg=st.navigation(
{
        "MainPage":[p1],
        "Analysis":[p2,p3,p4,p5,p6,p8,p10],
        "Predictions":[p7,],
        "FinalPage":[p9]
}
)
pg.run()