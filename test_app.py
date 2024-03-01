import streamlit as st
import pandas as pd

@st.cache
def calculate_bmi(weight, height):
    # Check if height is not zero to prevent division by zero error
    if height == 0:
        return 0
    # Convert height from cm to meters
    height_m = height / 100.0
    # Calculate BMI
    bmi = weight / (height_m ** 2)
    return bmi

def main():
    st.title('Simple Streamlit App with User Input and Dynamic Graph')

    # Load existing data or create a new DataFrame
    data = st.session_state.get('data', pd.DataFrame(columns=['Weight', 'Height', 'BMI']))

    # Add text input boxes for the user's name, weight, and height
    name = st.text_input('Enter your name', 'Your Name')
    weight = st.number_input('Enter your weight (kg)', min_value=0.0)
    height = st.number_input('Enter your height (cm)', min_value=0.0)

    # Check if the name is provided
    if name != 'Your Name':
        st.write(f"Hello, {name}!")

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")

        # Append user input data to DataFrame
        new_entry = {'Weight': weight, 'Height': height, 'BMI': bmi}
        data = data.append(new_entry, ignore_index=True)
        st.session_state.data = data  # Update the session state data

        # Plot the user input data using Streamlit's native plotting functions
        st.write("Graph of Weight, Height, and BMI")
        st.line_chart(data.set_index('Height')[['Weight', 'BMI']])

if __name__ == '__main__':
    main()
