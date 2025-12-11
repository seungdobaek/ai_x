# streamlit run 3_summaryWeb.py
import streamlit as st
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import os

def askGPT(prompt):
    "GPT에게 요청하여 prompt 내용을 1줄 요약하여 return"
    load_dotenv()
    client = OpenAI()
    response = client.chat.completions.create(
        model='gpt-5-nano',
        messages=[
            {'role':'system', 'content':'당신은 한국어로 된 텍스트를 잘 요약하는 전문어시스트입니다'},
            {'role':'user', 'content':prompt}
        ]
    )
    return response.choices[0].message.content

def main():
    load_dotenv()
    st.set_page_config(page_title="요약 프로그램")
    
    st.header('요약 프로그램')
    st.markdown('---')
    message = st.text_area('요약할 글을 입력하세요')
    if st.button('요약'):
        prompt =  f""" your task is to summarize the text sentences in Korean language. Summarize in 1 line. Use the format of a bullet point. text : {message}"""
        st.info(askGPT(prompt=prompt))

if __name__=='__main__':
    main()