"""
This file is the starting point of what the user sees when routed.
"""

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
It's a pleasure to introduce myself! I'm an aspiring AI researcher and current Georgia Tech CS student. Please navigate to the pages on the side if you'd like to learn more about me.

1. Portfolio: This page is where I showcase a sort of extended resume about myself. It includes basic resume aspects like education, experience, projects, and skills.
2. Quiz: Having nothing to do with CS, I really enjoy classical literature as a side hobby. I would like to think it gives me an edge in communicative and writing based soft skills in the office, but here is a fun mini-quiz I put together on a few of my favorite pieces of literature.

""")
