import streamlit as st

from src.screens.homescreen import homescreen
from src.screens.studentscreen import studentscreen
from src.screens.teacherscreen import teacherscreen
from src.components.auto_enroll_dialog import auto_enroll_dialog


def main():

    
    st.set_page_config(
        page_title="MyClass-AI Attendance System",
        page_icon="https://cdn-icons-png.flaticon.com/128/5609/5609505.png",
        
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    if st.session_state['login_type'] == 'Teacher':
        teacherscreen()

    elif st.session_state['login_type'] == 'Student':
        studentscreen()

    else:
        homescreen()
    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'Student':
            st.session_state.login_type = 'Student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)

main()