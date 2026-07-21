import streamlit as st
import info
import pandas as pd

#sidebar links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height = "75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    st.sidebar.text("Check out my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width = "65" height = "65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width = "75" height = "75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

links_section()

#education
def education_section(education_data, course_data):
    st.header("📖Education💻")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code":"Course Code",
        "names":"Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True,
        )
    st.write("---")

education_section(info.education_data, info.course_data)

#professional experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width = 250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(info.experience_data)

#projects section
def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")

project_section(info.projects_data)

#skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,)}")
        st.progress(percentage)

    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,)}: {proficiency}")

    st.write("---")
    
skills_section(info.programming_data, info.spoken_data)

#activities
def activities_section(award_data, ec_data):
    st.header("Achievements and Activities")
    tab1, tab2 = st.tabs(["Awards", "Extracurriculars"])
    with tab1:
        st.subheader("Awards")
        for title, (details, image) in award_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Extracurriculars")
        for title, details in ec_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")

activities_section(info.award_data, info.ec_data)

def exporting():
    st.header("Download My Resume")
    res_expander = st.expander("Stopford_Carrick_Resume")
    res_expander.write("Let me guess: you're so blown away by this website that you want to hire me immediately? Here's a PDF of my resume:")
    res_expander.write("https://drive.google.com/file/d/1nwkUKCzIKdk_QWENXnLdsEEr_TTUZZV-/view?usp=sharing")    
    st.write("---")

exporting()
