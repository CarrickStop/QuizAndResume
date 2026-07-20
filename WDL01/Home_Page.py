import streamlit as st
import info

# Title of App
st.title("CS' Personal Website")

#about me
def about_me_section():
    st.header("About me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")

about_me_section()

st.write("""
Welcome to our Streamlit Web Development Lab01 app! You can navigate between the pages using the sidebar to the left. The following pages are:

1. Phase II: This page offers a fun reading quiz to test out a user's knowledege on literary classics. Reading the greats from any time period is my number one personal hobby! 
2. Portfolio: This page is where I showcase a sort of extended resume about myself. It includes basic resume aspects like education, experience, projects, and skills.

""")

