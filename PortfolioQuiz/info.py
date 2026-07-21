"""
This file is where we modularly store all the text and specific routes to the information presented within the 'pages' folder. 
"""

#Basic introductory info for the home page
profile_picture = "PortfolioQuiz/Images/profile.jpeg"
about_me = "I'm Carrick Stopford. Since my initials are CS, you could say that I'm made for what I do!"


#All basic personal URLs for sidebar image icons
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#All other basic personal URLs
my_linkedin_url = "https://www.linkedin.com/in/carrickstopcs/"
my_github_url = "https://github.com/CarrickStop"
my_email_address = "carrickstopford@gmail.com"


education_data ={
    'Degree': 'BS in Computer Science',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': 'May 2029',
    'GPA': '3.69/4.0'
}

course_data = {
    "code":["CS 1301", "CS 1331", "MATH 1554"], 
    "names":["Intro to CS", "Intro to OOP", "Computational Linear Algebra"], 
    "semester_taken":["1st", "2nd", "2nd"],
    "skills":["Python, Streamlit, Pandas", "Java, Object Oriented Programming Intuition, Spring", "Linear Algebra, Algorithmic Intuition"],
    }

experience_data = {
    "Orion Defense Solutions LLC remote" : (["- Engineered a pipeline in Python to perform research and write reports autonomously for defense purposes", "- Architected an intelligent"
     + " document-ingestion pipeline that automatically"
     + " extracted and prioritized key engineering requirements from 20+ page government solicitation documents into structured, machine-readable datasets", "- Developed comprehensive unit"
     + " testing frameworks using Pytest and Pandas to structure proposal requirement datasets and automate LLM output evaluation against verified baselines, reducing regression defects by"
     + " 25%.", "- Designed and integrated an intuitive, customizable Streamlit frontend with a FastAPI backend to orchestrate end-to-end LDR workflows, connecting user inputs to modular LLM"
     + " services for automated proposal generation."], "PortfolioQuiz/Images/orion.jpeg"),
     "Information Technology and Repair Technician for Lifeline Repairs in Peachtree City, GA" : (["- Repaired over 110 computers, tablets, and phones", "- Diagnosed Countless Malfunctioning"
     + " Devices", "- Accumulated a concrete understanding of computer hardware and design"], "PortfolioQuiz/Images/lifeline.jpeg"),
     "PC Technician for Computech Systems in Fayetteville, GA" : (["- Built PCs from scratch", "- Upgraded customer PCs for optimized performance"],"PortfolioQuiz/Images/computech.png")
}

projects_data = {
    "AIO Finances (Collaborative, Ongoing)" : "AIO Finances "
}

programming_data = {
    "Python": 90,
    "Java": 90
}

programming_icons = {
    "Python": "🐍",
    "Java": "☕"
}
spoken_icons = {
    "English": "🦅",
    "German":"🍻"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "German": "Conversationally Acceptable"
}
award_data = {
    "Whitewater High School in Fayetteville, GA": (["- Valedictorian out of a 310 class size"],"PortfolioQuiz/Images/speech.jpeg"),

}
ec_data={
    "Georgia Tech in Atlanta, GA": ["- Georgia Tech Police Department intern, Student Government committee member, classic literature enthusiast"]
}
