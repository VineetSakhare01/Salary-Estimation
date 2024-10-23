# Salary Estimation 

This project is a Salary Estimation Application built using Streamlit and a machine learning model. The app predicts the salary of an employee based on input features like years of experience and job role. It uses a pre-trained model stored in a .pkl file and presents results via a simple web interface.

# Project Overview:
The Salary Estimation App provides an interactive interface for users to input their details and get a predicted salary. The app is powered by a machine learning model trained on employee attrition data and predicts salaries based on features such as years at the company, job role, etc.

# Features:
Predicts employee salary based on various factors.
Interactive and user-friendly web interface using Streamlit.
Uses a pre-trained machine learning model.
Easy to run and set up locally.

# Files in the Repository:

Salary.py: Contains the code for training and saving the salary prediction model.

app.py: The main file for running the Streamlit app.

employee_attrition_data.csv: The dataset used to train the model.

model.pkl: The saved machine learning model used for salary prediction.

scaler.pkl: The saved scaler for preprocessing numerical input data.

salaryprediction.ipynb: A Jupyter notebook containing the process for training and evaluating the model.

# Model Information:

The machine learning model used in this app is stored in the model.pkl file and was trained using scikit-learn. The model uses features such as:

- Years at the company
- Job role
- Other employee attributes from the employee_attrition_data.csv dataset

# Steps performed to Train the Model:

1. The model was trained using the employee_attrition_data.csv dataset, which contains various employee details.

2. A StandardScaler was applied to the numerical features, and this scaler is saved in scaler.pkl.

3. The model was saved as model.pkl for use in the Streamlit app.

4. The code for training and saving the model can be found in the Salary.py script and salaryprediction.ipynb notebook.





