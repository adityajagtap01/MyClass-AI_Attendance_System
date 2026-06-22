
import time

import streamlit as st

from Database.db import get_all_students,create_student
from pipelines.face_pipeline import get_face_embeddings, predict_attendance, train_classifier
from pipelines.voice_pipeline import get_voice_embedding
from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_home

import numpy as np
from PIL import Image





def student_dashboard():
    st.header('Dashboard page')

def studentscreen():


    style_background_dashboard()
    style_base_layout()


    if "student_data" in st.session_state:
        student_dashboard()
        return 
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    
    st.space()
    st.space()
    
    show_registration = False

    st.markdown(
    "<h1 style='color:black; text-align:center;'>Login Using FaceID</h1>",
    unsafe_allow_html=True
    )
    

    st.markdown(
    "<p style='color:black; font-size:18px;'>Position your face in the center</p>",
    unsafe_allow_html=True
)

    photo_source = st.camera_input("", label_visibility="collapsed")
    
    if photo_source:
        img=np.array(Image.open(photo_source))

        with st.spinner("AI is Scanning..."):

            detected,all_ids,num_faces=predict_attendance(img)

            if num_faces==0:
                st.warning("No face detected. Please try again.")
            elif num_faces>1:
                st.warning("Multiple faces detected. Please ensure only one face is visible.")

            else :
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id']==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student['name']}')
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.info('Face not recognized! You might be a new student!')
                        show_registration = True

        if show_registration:
                with st.container(border=True):
                    st.header('Register new Profile')
                    new_name = st.text_input("Enter your name", placeholder='E.g. Rohit Sharma')

                    st.subheader('Optional : Voice Enrollment')
                    st.info("Enroll your for voice only attendance")


                    audio_data = None

                    try:
                        audio_data = st.audio_input('Record a short phrase like I am present, My name is Rohit.')
                    except Exception:
                        st.error('Audio Data failed!')

                    if st.button('Create Account', type='primary'):
                        if new_name:
                            with st.spinner('Creating profile..'):
                                img = np.array(Image.open(photo_source))
                                encodings= get_face_embeddings(img)
                                
                                if encodings:
                                    face_emb = encodings[0].tolist()

                                    voice_emb = None
                                    if audio_data:
                                        voice_emb = get_voice_embedding(audio_data.read())

                                    response_data = create_student(new_name, face_embedding=face_emb, voice_embedding=voice_emb)

                                    if response_data:
                                        train_classifier()
                                        st.session_state.is_logged_in = True
                                        st.session_state.user_role = 'student'
                                        st.session_state.student_data = response_data[0]
                                        st.toast(f'Profile Created! Hi {new_name}!')
                                        time.sleep(1)
                                        st.rerun()
                                else:
                                    st.error('Couldnt capture your facial features for registration')

                        else:
                            st.warning('Please enter your name!')

    footer_home()