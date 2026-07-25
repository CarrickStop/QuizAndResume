"""
This file is the starting point of what the user sees when routed.
"""

import streamlit as st
import info

# Title of App
st.title("CS' Personal Website")

#about me
def about_me_section():
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("---")

about_me_section()

st.write("""
It's a pleasure to introduce myself! I'm an aspiring AI researcher and current Georgia Tech CS student. Please navigate to the pages on the side if you'd like to learn more about me.

1. Portfolio: This page is where I showcase a sort of extended resume about myself. It includes basic resume aspects like education, experience, projects, and skills.
2. Quiz: Having nothing to do with CS, I really enjoy classical literature as a side hobby. I would like to think it gives me an edge in communicative and writing based soft skills in the office, but here is a fun mini-quiz I put together on a few of my favorite pieces of literature.

""")

st.write("---")

st.write("""
**A glimpse into my mindset and the process that shaped it:**

Enduring stage IV Wilms tumor at a young age, I lived much of my early life not knowing whether
 or not certain challenges I faced were from irreparable side effects of the illness or just
 regular setbacks that could be overcome like anything else. Mostly these questions were
 physical, but it was made possible for me to use cancer as an all powerful excuse to
 justify anything within my family and community. I had learned of that power participating in
 sports as a middle schooler: my excuses were sympathetically accepted by those around me.
 But ultimately, I played sports because I sought the satisfication from a good competition,
 and sympathy did not magically grant me victories, only the permission to lose-. It was not
 long before I became disillusioned with seeking excuses because justified or not, they never
 changed the outcome. Reality does not bend for a great context. 
 
 I did end up learning from a doctor that endurance sports would in fact not be highly feasible
 as I was simply missing 60% of my lung capacity, but that did not stop me from finding
 competition in other sports and entirely new fields for a soon to be teenager, like academics
 where I would eventually become a valedictorian. The concluding mindset I have arrived at in
 life from cancer is that it does not really matter how to justify a problem when faced with it
 because, for any roadblock life confronts me with going forward, I am always certain that there
 is another route.
""")
