# 🏥 Healthcare Analytics Dashboard

This **Healthcare Analytics Dashboard** is an interactive **Streamlit** application that provides insightful visualizations and machine learning predictions based on healthcare data. It helps analyze various factors such as **BMI, Age, Smoking Habits, Regional Distribution, and Correlation Analysis** while also offering predictive analytics for **medical charges**.

---

## 🚀 Features

- **📊 Data Analysis**
  - **BMI Analysis** - Understand how BMI affects charges and smoking habits.
  - **Age Segmentation** - Analyze healthcare trends across different age groups.
  - **Regional Analysis** - Explore variations in healthcare charges based on region.
  - **Smoker Analysis** - Compare charges between smokers and non-smokers.
  - **Doctor Satisfaction** - Assess patient satisfaction across different doctors.
  - **Correlation Analysis** - Identify relationships between various healthcare parameters.
  - **Time-Series Analysis** - Examine trends over time.

- **🔮 Predictive Modeling**
  - Uses **Linear Regression, Decision Tree, Random Forest, and Support Vector Regressor (SVR)** to predict medical charges.
  - Compares model performance using **Mean Absolute Error (MAE) & Mean Squared Error (MSE)**.

- **📌 Interactive UI**
  - **Wide-layout** dashboard using **Streamlit Themes**.
  - **Navigation Bar** to switch between pages easily.
  - **Data-driven visualizations** with **Plotly** and **Streamlit Extras**.

---

## 📦 Installed Packages

- **streamlit**
- **pandas**
- **plotly**
- **numpy**
- **scikit-learn**
- **streamlit-themes**
- **streamlit-extras**
- **streamlit-shadcn-ui**

---

## 📈 Model Performance

- **Training & Testing Data:** The dataset includes attributes such as `age`, `bmi`, `smoker`, and `charges`.
- **Model Comparison:** The application displays performance metrics for each model using interactive charts.
- **User Prediction:** Users can input their **age**, **BMI**, and **smoking status** to get a predicted estimate for their medical charges.

---

## 🛠 Installation & Usage

### 1️⃣ Install Dependencies
Ensure you have **Python 3.7+** installed. Then, install the required packages:

```bash
pip install streamlit pandas plotly numpy scikit-learn streamlit-themes streamlit-extras streamlit-shadcn-ui

### 2️⃣ Run the Application
To launch the dashboard, run:

```bash
streamlit run app.py

### 3️⃣ Explore the Dashboard
Open your browser to the local URL provided by Streamlit, and navigate through the different pages using the built-in navigation sidebar.

---

## 🌐 Live Demo
Access the hosted dashboard on the Streamlit Community Cloud:

[Healthcare Dashboard Live][https://healthcare-dashboard.streamlit.app/]

---
##💡 Insights and Learnings
Throughout the development of this dashboard, several key insights and learnings emerged:

- Data Visualization is Crucial: Interactive charts and graphs significantly enhance user understanding and engagement.
- Model Comparison Enhances Reliability: Comparing multiple machine learning models helps in selecting the best predictor based on performance metrics.
- User-Centric Design: An intuitive navigation system and clear layout improve overall user experience.
- Continuous Improvement: Feedback from real users is essential to further refine the analysis and prediction models.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to enhance this project, feel free to fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you'd like to change.

