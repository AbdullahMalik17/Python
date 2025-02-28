import streamlit as st

# Title of the app
st.title("Poultry Farm Management")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ["Home", "Add Chicken", "View Chickens"])

# Home page
if options == "Home":
    st.header("Welcome to the Poultry Farm Management App")
    st.write("Use the navigation menu to add or view chickens.")

# Add Chicken page
elif options == "Add Chicken":
    st.header("Add a New Chicken")
    with st.form("add_chicken_form"):
        name = st.text_input("Chicken Name")
        age = st.number_input("Age (in weeks)", min_value=0)
        breed = st.text_input("Breed")
        submit = st.form_submit_button("Add Chicken")
        
        if submit:
            st.write(f"Chicken {name} added successfully!")

# View Chickens page
elif options == "View Chickens":
    st.header("View All Chickens")
    # This is a placeholder for where you would display the list of chickens
    st.write("List of chickens will be displayed here.")