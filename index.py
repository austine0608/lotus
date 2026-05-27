import streamlit as st


st.set_page_config(page_title = 'Makintouch')
st.title('My Story Album')
st.markdown('---')
st.markdown('''
**My Story Album** is a creative and interactive landing page designed to preserve, 
showcase, and celebrate personal memories, experiences, and life moments in a 
beautiful digital format. The platform allows users to organize their stories, 
photos, videos, and memorable events into a visually appealing album that captures 
their journey and emotions. With a modern and user-friendly interface, My Story Album 
creates a personalized storytelling experience where every memory becomes meaningful 
and easy to relive. It serves as a digital space for inspiration, connection, and 
timeless storytelling.
''')
st.markdown('---')
col1, col2, col3 = st.columns(3)

with col1:
    st.caption('A Weeping Woman')
    st.image('./images/1.png')
with col2:
    st.caption('Lady Crying')
    st.image('./images/2.png')
with col3:
    st.caption('Happy Relationship')
    st.image('./images/3.png')
with col1:
    st.caption('Lagos')
    st.image('./images/4.png')
with col2:
    st.caption('Gossip')
    st.image('./images/5.png')
with col3:
    st.caption('A Fashion Designer')
    st.image('./images/6.png')
st.audio('./images/2.mp3')
st.markdown('---')
st.markdown('''
        <h6 style="background-color:gray;border-radius:10px;padding-left:200px;padding-top:20px">
            Makintouch Consulting Copywrite@2026
            </h6>
''',
unsafe_allow_html = True)
st.markdown('---')