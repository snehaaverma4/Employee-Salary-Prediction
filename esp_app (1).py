# -*- coding: utf-8 -*-
"""esp-app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10xbbGETrlnU2lGAQDzAvIHvKm_y7r1cw
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Salary Predictor 💼", page_icon="📊", layout="centered")

st.markdown("""
    <h1 style='color:#4CAF50;'>Employee Salary Predictor 💰</h1>
    <h4 style='color:#555;'>Estimate salary based on job profile, education & experience</h4>
    <hr style='border:1px solid #eee' />
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    education = st.selectbox("🎓 Education Level", ['Bachelors', 'Masters', 'PhD'])

with col2:
    job_title = st.selectbox("💼 Job Title", ['Software Engineer', 'Data Scientist', 'HR Manager', 'Sales Associate'])

experience = st.slider("📅 Years of Experience", 0, 40, step=1)

# ✅ Move this OUTSIDE the button so it's available globally
base_salary = {
    'Software Engineer': 60000,
    'Data Scientist': 70000,
    'HR Manager': 50000,
    'Sales Associate': 45000
}

multiplier = {
    'Bachelors': 3000,
    'Masters': 4000,
    'PhD': 5000
}

# 🎯 Prediction block
if st.button("🚀 Predict Salary"):
    predicted_salary = base_salary[job_title] + (experience * multiplier[education])

    st.markdown(f"""
        <div style='
            padding: 1em; 
            background-color: #1e5128; 
            border-left: 5px solid #a6f4a4;
            border-radius: 8px;
            margin-top: 10px;
        '>
            <h2 style='color: #ffffff; font-size: 28px;'>
                💸 Estimated Salary: ₹{int(predicted_salary):,}
            </h2>
        </div>
    """, unsafe_allow_html=True)



# 📊 Graph block
with st.expander("📈 Show Experience vs Salary Trend"):
    exp_range = list(range(0, 31))
    trend_salary = [base_salary[job_title] + (x * multiplier[education]) for x in exp_range]

    fig, ax = plt.subplots()
    ax.plot(exp_range, trend_salary, color='#4CAF50', linewidth=2)
    ax.set_title("Experience vs Salary")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Estimated Salary (₹)")
    st.pyplot(fig)

st.markdown("""<hr style="border:1px solid #eee" />""", unsafe_allow_html=True)
st.markdown("Made by Sneha Verma | [GitHub](https://github.com/snehaaverma4/Employee-Salary-Prediction)")
