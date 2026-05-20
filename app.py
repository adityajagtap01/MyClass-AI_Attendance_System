import streamlit as st

from src.screens.homescreen import homescreen
from src.screens.studentscreen import studentscreen
from src.screens.teacherscreen import teacherscreen


def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    if st.session_state['login_type'] == 'Teacher':
        teacherscreen()

    elif st.session_state['login_type'] == 'Student':
        studentscreen()

    else:
        homescreen()


main()