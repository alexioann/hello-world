import streamlit as st
import pandas as pd

def main():
    st.title('User Data and Age Histogram')

    # Load existing data or create a new DataFrame
    data = st.session_state.get('data')
    if data is None:
        data = pd.DataFrame(columns=['Name', 'Age'])

    # Add text input boxes for the user's name and age
    name = st.text_input('Enter your name', 'Your Name')
    age = st.number_input('Enter your age', min_value=0)

    # Check if the name is provided
    if name != 'Your Name':
        st.write(f"Hello, {name}!")

        # Append user input data to DataFrame
        new_entry = {'Name': name, 'Age': age}
        data = data.append(new_entry, ignore_index=True)
        st.session_state.data = data  # Update the session state data

        # Create a histogram to display the distribution of ages
        st.write("Age Histogram")
        st.bar_chart(data['Age'].value_counts())

if __name__ == '__main__':
    main()
