import streamlit as st
import numpy as np
import pickle
import os

# Correct the model path assignment
model_path = os.path.join(os.path.dirname(__file__), 'linear_regressor_model.pkl')

# Load the model
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Salary Automatization App")

# Add a brief description
st.write("This app predicts the salary based on years of experience using a simple linear regression model.")

# Input from user
years_experience = st.number_input("Enter years of experience", min_value=0, max_value=50, value=1)

# When the button is clicked, make predictions
if st.button("Predict Salary"):
    # Make a prediction using the trained model
    input_array = np.array([[years_experience]])
    predicted_salary = model.predict(input_array)

    # Display the result
    st.success(f"The predicted salary for {years_experience} years of experience is ${predicted_salary[0]:,.2f}")

# Footer note
st.write("Note: This is a simple linear regression model and may not reflect real-world complexities.")

