import streamlit as st
import requests

st.title("🤖 简单AI助手")

# 从Streamlit Secrets读取API Key（部署时在云端设置）
api_key = st.secrets["DEEPSEEK_API_KEY"]

prompt = st.text_input("请输入你的问题：")

if prompt:
    with st.spinner("正在思考..."):
        url = "https://api.deepseek.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
            st.success(answer)
        else:
            st.error(f"API错误：{response.status_code}")