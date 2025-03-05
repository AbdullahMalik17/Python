import streamlit as st 
st.title('Unique Boutique')
st.write('Welcome to Unique Boutique! We are a boutique that sells unique items.')
st.sidebar.title('Navigation')
st.sidebar.write('Select a page:')
page = st.sidebar.radio('goto',['Home','Contact Us','About Us'])
if page == 'Home':
    st.write('Welcome to the Home page')
    st.write('We Built very interactive clothes')
elif page == 'Contact Us':
    st.text_input('Enter your Name').placeholder('Name')
    st.text_input('Enter your Email').placeholder('Email')    
    st.text_area('Enter your Message').placeholder('Enter your Comments')
    st.button('Submit')
else:
    st.write('Welcome to the About Us page')    