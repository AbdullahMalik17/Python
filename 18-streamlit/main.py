import streamlit as st 
st.title('Unique Boutique'
st.write('Welcome to Unique Boutique! We are a boutique that sells unique items.')
st.sidebar.title('Navigation')
st.sidebar.write('Select a page:')
page = st.sidebar.radio('goto',['Home','Contact Us','About Us'])
if page == 'Home':
    st.write('Welcome to the Home page')
    st.write('We Built very interactive clothes')
    st.image('https://images.unsplash.com/photo-1606780840004-4b0b7e3f3b3b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60')
elif page == 'Contact Us':
    st.text_input('Enter your Name')
    st.text_input('Enter your Email')    
    st.text_area('Enter your Message')
    st.button('Submit')
else:
    st.write('Welcome to the About Us page')    