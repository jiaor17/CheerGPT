from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st

openai_api_key = st.sidebar.text_input('OpenAI API Key')
model_name = st.sidebar.selectbox('Model', ("gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4"))

st.title("CheerGPT")

template = """
请夸夸我！
你可以叫我：{id}
我的近况：{cur}
"""



pid = st.text_input("怎么称呼您?","")
cur = st.text_area("最近过得怎么样!", "")


prompt = PromptTemplate.from_template(template)
ipt = prompt.format(id=pid, cur=cur)


chat_model = ChatOpenAI(temperature=0, model_name=model_name, openai_api_key=openai_api_key)


if st.button("快夸夸我！"):
    with st.spinner("别急别急"):
        result = chat_model.predict(ipt)
        st.success(result)
        st.balloons()

