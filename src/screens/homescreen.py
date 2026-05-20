import streamlit as st
from src.ui.base_layout import style_base_layout
from src.ui.base_layout import style_background_home
from src.components.header import header_home
from src.components.footer import footer_home   

def homescreen():

    header_home()
    style_background_home()
    style_base_layout()
  
    col1,col2 = st.columns(2,gap="large")
    with col1:
          
          st.markdown("<h2 style='color:#000080;'>I'm Student</h2>", unsafe_allow_html=True)
          st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
          if st.button('Student Portal', type='primary', icon=':material/arrow_outward:,icon_position='right'):
            st.session_state['login_type']='Student'
            st.rerun()
    with col2:
       
        st.markdown("<h2 style='color:#000080;'>I'm Teacher</h2>", unsafe_allow_html=True)
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:',icon_position='right'):
            st.session_state['login_type']='Teacher'
            st.rerun()







    footer_home()