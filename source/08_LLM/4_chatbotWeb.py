import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()
    st.set_page_config(page_title='비추 챗봇')
    st.title('비추 챗봇')

    # 대화이력 초기화
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {'role':'system', 'content':'당신은 친절한 AI 챗봇입니다. 최대한 간결하고 짧게 유저에게 답변해주세요'},
        ]
    
    # 대화 이력 표시(system 메세지 제외)
    for msg in st.session_state.messages[1:]:
        st.chat_message(msg['role']).write(msg['content'])
    
    # 사용자 질문 입력받아 질문하기
    if prompt := st.chat_input('메세지를 입력하세요'):
        # 사용자 질문을 세션에 추가하고 출력
        prompt = prompt.strip()
        st.session_state.messages.append({'role':'user', 'content':prompt})
        st.chat_message('user').write(prompt)

        #AI 응답을 받아 session 추가하고 출력
        client = OpenAI()
        response = client.chat.completions.create(
            model = "gpt-5-nano",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        reply = reply.strip()
        st.session_state.messages.append({'role':'assistant', 'content':reply})
        st.chat_message('assistant').write(reply)

if __name__=='__main__':
    main()