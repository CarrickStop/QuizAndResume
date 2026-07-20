import streamlit as st

##Instructions:
##Must include a minimum of five questions.
##Must include three different types of questions. For example, one multi-select, one multiple
##choice, and one number input.
##Must include at least 3 images.
##Must use at least 3 streamlit functions that weren't used in Section 1 with a #NEW comment
##next to each of them.
##Here are a few examples:
##st.radio
##st.selectbox
##st.multiselect
##st.slider
##st.number_input
##st.progress
##st.metric
##st.balloons()
##st.audio
##st.image - this should not be considered new, it was in the portfolio
##If you use modules that are not part of the Python Standard Library ( math , random , etc.), you
##must list out all of the modules that must be installed for your app to work in
##requirements.txt , one module per line. Streamlit and Pandas are already included in the
##requirements.txt file that is provided.

correctTotal = 0

def multipleChoiceCrime():
    global correctTotal
    rightCrime = 1
    ans = st.radio("Amongst the options, what could be said to be the genre of \"Crime and Punishment\" by Fyodor Dostoevsky?",
                         ["Romantic", "Trascendentalist", "Neo-Classical", "Existentialist"]) #NEW
    if ans == "Existentialist":
        correctTotal += 1
    else:
        rightCrime -= 1
    st.image("https://cdnb.artstation.com/p/assets/images/images/081/757/287/large/anastasia-kaluzhnaya-2.jpg?1731132813", width = 200)
    st.write("A conceptualization of the book's protagonist Raskolnikov and his murder weapon")
    st.write("Art credit: Anastasia Kaluzhnaya on https://www.artstation.com/artwork/lDo4Gk")
    st.write("---")
    
multipleChoiceCrime()

def multiSelectFrank():
    global correctTotal
    rightFrank = 1
    choices = st.multiselect("Regarding Mary Shelley and her novel \"Frankenstein,\" select every true choice:",
                             ["The Monster attempts to negotiate with Dr. Frankenstein", "The Monster immiediately creates destruction upon his conception",
                              "The Monster is supremely intelligent and scientifically marvelous",
                              "Mary Shelley is the only 'celebrity' amongst her immediate family members"]) #NEW
    choicesCList = ["The Monster attempts to negotiate with Dr. Frankenstein", "The Monster is supremely intelligent and scientifically marvelous"]
    choicesCListOther = ["The Monster is supremely intelligent and scientifically marvelous", "The Monster attempts to negotiate with Dr. Frankenstein"]
    if choices == choicesCList or choices == choicesCListOther:
        correctTotal += 1
    else:
        rightFrank -= 1
    st.image("https://www.meisterdrucke.us/kunstwerke/1260px/Unknown_Artist_-_Industrial_Revolution_-_Industrial_Revolution_Overview_of_Mr_Vivians_copper_plan_-_%28MeisterDrucke-914415%29.jpg", width = 200)
    st.write("The discontentment of the first industrial revolution would lead to \"Frankenstein\" being written.")
    st.write("Art credit: \"The Copper Plant Painting\" by an unknown artist, 1865")
    st.write("---")

multiSelectFrank()

def numCities():
    global correctTotal
    rightCities = 1
    #NEW below
    ans = st.number_input("Charles Dickens' \"A Tale of Two Cities\" depicts juxtaposing perspectives on the French Revolution, and Dickens both lauds its sense of justice and critiques its brutality. What year did this historic revolution begin that he so analyzes?")
    if ans == 1789.0 or ans == 1789:
        correctTotal += 1
    else:
        rightCities -= 1
    st.image("https://victorianweb.org/art/illustration/barnard/ttc/10.jpg", width = 200)
    st.write("Lord Evremonde is stabbed and killed in the night")
    st.write("Art credit: scanned by Philip V. Allingham in https://victorianweb.org/art/illustration/barnard/ttc/10.html")
    st.write("---")

numCities()        

def boolInvis():
    global correctTotal
    rightInvis = 1
    ans = st.radio("Regarding Emily Brontë's \"Wuthering Heights,\" the character of Heathcliff is known to easily let the 'past stay in the past.'", ["True", "False"])
    if ans == "False":
        correctTotal += 1
    else:
        rightInvis -= 1
    st.image("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/13ad574a-d285-4777-b06c-c1bfd5db9166/d9gwiow-c6727545-6945-47ea-a051-5e2408a406bd.jpg/v1/fill/w_1024,h_1882,q_75,strp/heathcliff_concept_by_muirin007_d9gwiow-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTg4MiIsInBhdGgiOiIvZi8xM2FkNTc0YS1kMjg1LTQ3NzctYjA2Yy1jMWJmZDVkYjkxNjYvZDlnd2lvdy1jNjcyNzU0NS02OTQ1LTQ3ZWEtYTA1MS01ZTI0MDhhNDA2YmQuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.DFatY-s06KrB14C4sYxh4FsDtwSKYr5xtlPMSS2GRiI", width = 200)
    st.write("This fan made depiction is a close visualization of the character of Heathcliff based off how he's described in the book.")
    st.write("Art credit: 'Muirin2007' on DeviantArt.com https://www.deviantart.com/muirin007/gallery")
    st.write("---") 

boolInvis()

def enjoyment():
    global correctTotal
    rightEnjoy = 1
    ans = st.radio("Do you like reading? (You will lose a point if you answer no)", ["YES", "no.."])
    if ans == "YES":
        correctTotal += 1
    else:
        rightEnjoy -= 1
    st.write("---") 

enjoyment()

if st.button("Submit"): #NEW
        st.write(f"You scored a {correctTotal}/5.")
        st.write("Answers:")
        st.write("\"Crime and Punishment\" is actually Existentialist by genre. It is not apart of the official philosophical/literary movement, but Raskolnikov's navigation through a feeling of moral superioty matches the societally isolated themes of Existentialism.")
        st.write("Frankenstein's Monster tried to make a deal with the doctor to create a lover, and if the doctor abided, the Monster would have been peaceful. The Monster doesn't commit crime until he is abhorred. Representative of scientific achievement, the Monster is smart and impressive yet considered grotesque. Mary Shelley's mother Mary Wollstonecraft was a renonwed feminist leader.")
        st.write("Heathcliff's most basic characterization is actually that he does not let anything go, whether it be love, resentment, or pride.")
