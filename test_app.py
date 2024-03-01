import streamlit as st
import numpy as np
import pandas as pd

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height_m = height / 100.0
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi

def main():
    st.title('Simple Streamlit App with User Input and Random Graph')

    # Add text input boxes for the user's name, weight, and height
    name = st.text_input('Enter your name', 'Your Name')
    weight = st.number_input('Enter your weight (kg)', min_value=0.0, value=70.0)
    height = st.number_input('Enter your height (cm)', min_value=0.0, value=170.0)

    # Check if the name is provided
    if name != 'Your Name':
        st.write(f"Hello, {name}!")

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Generate random data for weight, height, and BMI
        np.random.seed(0)
        n_samples = 100
        weights = np.random.normal(weight, 5, n_samples)
        heights = np.random.normal(height, 10, n_samples)
        bmis = calculate_bmi(weights, heights)

        # Create a DataFrame
        data = pd.DataFrame({'Weight': weights, 'Height': heights, 'BMI': bmis})

        # Plot the data using Streamlit's native plotting functions
        st.write("Random Graph of Weight, Height, and BMI")
        st.line_chart(data[['Weight', 'Height', 'BMI']])

if __name__ == '__main__':
    main()
