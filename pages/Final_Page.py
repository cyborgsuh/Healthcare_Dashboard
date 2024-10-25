import streamlit as st

# Set up the final page title
st.title("Thank You for Exploring the App!")

# Thank you message and final thoughts
st.write(
    """
    ### Your Exploration Matters!
    Thank you for taking the time to explore the data and insights provided by this app.
    Your interest and curiosity are what drive innovation and discovery.

    I hope you found value in the analyses and visualizations, whether it was the 
    **Age-based Segmentation**, **BMI Analysis**, or any of the other insightful sections.

    ### Stay Connected!
    I'm always looking to improve and expand, so feel free to reach out with any feedback, suggestions, or questions. Your input is invaluable.
    """
)

# Feedback options using radio buttons
st.write("How would you rate your experience with the app?")
experience_rating = st.radio(
    "Choose an option:",
    ("Excellent", "Good", "Average", "Poor")
)

# Suggestions for improvement using checkboxes
st.write("What improvements would you like to see?")
improvements = st.multiselect(
    "Select all that apply:",
    ["More Visualizations", "Additional Data Analysis", "User Interface Enhancements", "More Interactive Features"]
)

# Submit button for feedback
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback! 😊")
    st.write(f"**Experience Rating:** {experience_rating}")
    st.write(f"**Suggested Improvements:** {', '.join(improvements) if improvements else 'None'}")

# Optional links section
st.markdown(
    """
    - [GitHub Repository](https://github.com/cyborgsuh)
    - [LinkedIn](https://www.linkedin.com/in/mosuh64)
    """
)

# Centered Credits footer
st.markdown(
    """
    <div style='text-align: center;'>
        <p>Developed by Suhaib | Powered by Streamlit</p>
    </div>
    """, unsafe_allow_html=True
)
