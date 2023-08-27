#importing libraries 
'''streamlit for UI
and the langchain is the wrapper for accessing the LLM's '''
import streamlit as st
from langchain.llms import HuggingFaceHub 
import os
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

#this piece of code is to remove the made with streamlit command
st.markdown("""
<style>

.css-cio0dv egzxvld1
{
    visibility : hidden;
}


</style>
""" , unsafe_allow_html = True)
#creating the user interface- "the sidebar"

with st.sidebar:
    st.image("qalogo.jpg")
    st.title("┗┃・ ■ ・┃┛ QA-GPT!!")
    menu = st.radio("Menu" ,["Home", "QA-App", "About Me"])

#home menu to display the home section 
if menu == "Home":
    st.title("Welcome to the Q/A-GPT.")
    st.header("This is a Generative AI application which will answer few of your basic questions.")
    st.subheader("Steps to follow")
    list_items=''' 
    1. Click on the QA-App button and navigate to the QA section.\n
    2. In the QA-App section in the input text box, type in your basic question.\n
    3. The generative AI-System will generate the answer for your question.'''
    st.write(list_items) 

#the qa section where the llm app will run 
if menu == 'QA-App':
    st.title("┗┃・ ■ ・┃┛ Welcome to QA-GPT 😉")
    st.header("This application will answer to few of your basic questions 😄")
    
    question = st.text_input("Please type your question here:")
    llm = HuggingFaceHub(repo_id='google/flan-t5-xxl')
    answer = llm(question)

    submit = st.button("Generate Answer") 

    if submit:
        st.subheader("👉 Here is your generated answer:")
        st.write(answer)


if menu == "About Me":
    st.title("@ ABOUT ME!! 📌")
    st.text("""Self-driven and Aspiring Engineer, Currently involved myself in the stream of 
Artificial intelligence.Passionate and Thriving Engineer Who Can Apply Techniques for data driven 
decision making and Knowledge to Develop and Solve Real-World Industry Problem by Adding Value to it.\n
My path for Artificial Intelligence started in 2020 where I was attracted to the way it functions. 
Since then my keen and interest in AI has never been down and wanted to contribute and provide solutions 
in this domain. For sure in the near future, I will be on my way contributing to this field and currently
working on becoming an Artificial Intelligence Engineer.Seeking to use my skills and knowledge to make
a positive impact as a data scientist.""")
    st.markdown("[Portfolio](https://impartial-wealth-154607.framer.app/)")
    st.markdown("[Git-Hub](https://github.com/KaRtHiK-56)")
    st.markdown("[Blog](https://sites.google.com/view/karthikaiblogs/home)")
    st.markdown("[Personal Instagram](https://www.instagram.com/prince_6_karthik/)")
    st.markdown("[Instagram](https://www.instagram.com/_.pythonista._/)")
    st.markdown("[Medium](https://karthikvegeta.medium.com/)")
    st.text("Gmail : karthiksurya611@gmail.com")
    st.text("⚡ Fun fact: I got inspired by Tony Stark ✌️ and Motivated by 💪 Prince Vegeta ♕")