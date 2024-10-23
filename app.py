
import streamlit as st
import joblib
import numpy as np

st.title("Salary Estimation App by Vineet")

st.divider()

Years_at_Company = st.number_input("Enter years at company: ", min_value=0, max_value=30)
Satisfaction_Level = st.number_input("Satisfaction Level: "min_value= 0.0)
Average_Monthly_Hours = st.number_input("Average Monthly Hours: ", min_value=0)

x = [Years_at_Company,Satisfaction_Level,Average_Monthly_Hours]

scaler = joblib.load("scaler.pkl")
model =  joblib.load("model.pkl")

predict_button = st.button("Press to predict the Salary!")

st.divider()

if predict_button:
    st.balloons()
    x1 = np.array(x)
    x_array = scaler.transform([x1])
    prediction = model.predict(x_array)[0][0]
    st.write(f"Salary Prediction is {prediction}")
else:
    st.write("Please enter the values & press the predict button")






