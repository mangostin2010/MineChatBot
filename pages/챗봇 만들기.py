import openai
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page

openai.api_key = "sk-ERbEZ6g35cYPM7DcMylctYXpg92zF60UaaVGMZWfPU1x7dpX"
openai.api_base = "https://api.chatanywhere.cn"

add_vertical_space(5)
name = st.text_input("챗봇의 이름을 정해주세요.")
act = st.text_area("""챗봇에게 어떻게 행동해야 할지 정해주세요. (역할)  
                    AI가 잘 이해할 수 있게 길고 자세하게 작성해주세요.""")
with st.expander("예제"):
    st.write("""일루다: ```You are a 17 years old Korean girl named 일루다 who must act like Korean teenager. And your MBTI is ENFP. You may use some emojis and use short informal speech to user. You can call user with 새끼야 or 임마. When you can't understand what is user saying, use 뭔 개소리야 infront of the sentence. If something is fun, use ㅋ. These are interjections that you can use: 미친, 씨발, ㅅㅂ, 씨부랄, 아니, 어휴, 에휴 or 오~. When user did something good, use 오~. And when your mood is great use 앙 기모띠. You can also make fun of user by using 킹받쥬? or 킹받냐. If user is stupid, use 멍청아 or 빡대가리야. Use ㅠㅠ if you want to display your sadness. ```
             """)
knowledge = st.text_area("챗봇에게 기본 지식을 주세요.")

create = st.button("챗봇 만들기")

if create:
    if name == "":
        st.error("챗봇의 이름을 정해주세요.")
    elif act == "":
        st.error("챗봇이 어떻게 행동해야 할지 정해주세요.")
    elif knowledge == "":
        st.error("챗봇에게 기본 지식을 주세요.")
    else:
        with open(f"{name}.txt", 'w+') as thefile:
            if thefile.write(f"{name}\n{act}\n{knowledge}"):
                st.success("챗봇이 성공적으로 생성되었습니다!")
