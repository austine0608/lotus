import streamlit as st 

st.title('Lotus-Gold Consulting Video Hub')
st.markdown('---')
st.video('./images/7.mp4')
st.markdown('---')
col1, col2, col3 = st.columns(3)

with col1:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/1.mp4')
with col2:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/6.mp4')
with col3:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/2.mp4')

with col1:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/3.mp4')
with col2:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/4.mp4')
with col3:
    st.caption('Lotus-Gold Consulting')
    st.video('./images/5.mp4')
st.markdown('---')
st.markdown('''  
       <h6 style="background-color:gray;border-radius:10px;padding-left:200px;padding-top:20px">
            Makintouch Consulting Copywrite@2026
            </h6>
''',
unsafe_allow_html = True)
st.markdown('---')
