import streamlit as st 


st.title('Contact Form')
with st.form('My Contact Form'):
    col1, col2 = st.columns(2)

  
    with col1:
        First_Name = st.text_input('Enter Your First Name')
    with col2:
        Last_name = st.text_input('Enter Your Last Name')
    with col1:
        Email_Address = st.text_input('Enter Your Email Address')
    with col2:
        Phone_number = st.number_input('Enter Your Phone Number')
    Message = st.text_area('Description')
    submmit = st.form_submit_button('Submit Info')