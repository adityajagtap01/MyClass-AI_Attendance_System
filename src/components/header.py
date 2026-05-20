import streamlit as st

def header_home():
   
    logo_url="https://cdn-icons-png.flaticon.com/128/5609/5609505.png"

    st.markdown(f"""
              <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
                
                <img src="{logo_url}" alt="Logo" style="height: 100px;">
                <h1 style='text-align: center; color:#E0E3FF;'>My<br/>Class</h1>
                
              </div>




                """, unsafe_allow_html=True)