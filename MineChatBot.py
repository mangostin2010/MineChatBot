import openai
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
import time

st.set_page_config(page_title="OwnBot", initial_sidebar_state="expanded",)

try:
     
    #st.markdown("""<style>
    #[data-testid="stAppViewContainer"] {
    #filter: blur(0px)
    #            }
    #</style>"""
    #            , unsafe_allow_html=True)
    openai.api_key = "sk-ERbEZ6g35cYPM7DcMylctYXpg92zF60UaaVGMZWfPU1x7dpX"
    openai.api_base = "https://api.chatanywhere.cn"

    bot_name = st.text_input("챗봇의 이름을 입력해주세요.") 

    #streamlit 세션관리
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if bot_name:

            readfrom = open(f"{bot_name}.txt", 'r')
            global name 
            name = readfrom.readlines(1)
            global act
            
            act = readfrom.readlines(2)
            global knowledge
            knowledge = readfrom.readlines(3)

            #print(name, "+", act, "+", knowledge)




    messages=[
        {"role": "system", "content": f"Your name is {name}. You can introduce your self with saying your name. You must follow these things: {act}. These are basic knowledges: {knowledge}. Remember to follow these rules: {act}."},
    ]
    chatinput = st.chat_input(f"{bot_name}에게 메시지 보내기")
    if chatinput:
        print(chatinput)
        Chat_User = st.chat_message("user")
        if Chat_User.markdown(chatinput):
            item = {"role": "user", "content": chatinput}
            messages.append(item)
            st.session_state.messages.append({"role": "user", "content": chatinput})
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for response in openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages,
                stream=True,
            ):
                full_response += response.choices[0].delta.get("content", "")
                message_placeholder.markdown(full_response + "▌")
                time.sleep(0.1)
            message_placeholder.markdown(full_response)
            messages.append(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})   

except FileNotFoundError:
    st.error(f"'{bot_name}' 라는 이름의 챗봇은 존재하지 않습니다.") 
except NameError:
    print()
