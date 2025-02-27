import streamlit as st 
st.title('Simple Streamlit App')

# Create a slider widget
x = st.slider('Select a value for x', 0, 100, 50)

# Display the selected value
st.write(f'The selected value for x is {x}')
