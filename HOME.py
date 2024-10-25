import streamlit as st
import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui



df=pd.read_csv("dataset.csv")
# Set the title of the home page
st.title("Medical Insurance Dataset Overview")

# Brief details about the dataset
st.markdown("""
    This dataset contains information about individuals, their health-related attributes (like BMI, smoker status), 
    and the insurance charges incurred. It includes the following features:
    
    - **Age**: Age of the individual.
    - **Sex**: Gender of the individual.
    - **BMI**: Body Mass Index of the individual.
    - **Children**: Number of children/dependents covered by health insurance.
    - **Smoker**: Whether the individual is a smoker or non-smoker.
    - **Region**: Geographic region of the individual.
    - **Charges**: Medical insurance cost charged.
    - **Customer Satisfaction**: Satisfaction level (1 to 5) of the customer.
    - **Customer Revisit**: Number of revisits.
""")



total_charges = df['charges'].sum()
avg_satisfaction = df['customer_satisfaction'].mean()
total_revisit_rate = df['customer_revisit'].mean()

st.subheader("Key Metrics")

# Create a layout for the 3 metrics using columns
cols = st.columns(3)

with cols[0]:
    ui.metric_card(
        title="Total Charges",
        content=f"${total_charges / 1_000_000:.0f}M",  
        description='Sum of all charges'
    )

with cols[1]:
    ui.metric_card(
        title="Customer Satisfaction",
        content=f"{avg_satisfaction:.1f}/5",  # Average satisfaction formatted to 2 decimals
        description='Average satisfaction score'
    )

with cols[2]:
    ui.metric_card(
        title="Total Revisit Rate",
        content=f"{total_revisit_rate:.2f}",  # Average revisit rate formatted to 2 decimals
        description='Average revisit'
    )


# Display the dataset
st.subheader("Dataset")
st.dataframe(df)

# Show the null values in the dataset
st.subheader("Null Values Summary")
null_df=pd.DataFrame(df.isna().sum(),columns=['Missing Values'])
st.dataframe(null_df,use_container_width=True)

# Display descriptive statistics of the dataset
st.subheader("Dataset Description")
st.dataframe(df.describe(), use_container_width=True)


st.header("What's Next!!!")
st.markdown('''
            The detailed evaluation is given in the pages with easy to understand and intuitive graphs and charts.
            Please click on the sidebar to navigate to the pages.
            ''')


