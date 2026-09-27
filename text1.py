import streamlit as st          
from openai import OpenAI   
    
st.set_page_config(page_title="Hello, I am the Mirror of Falsity, the Nightmare Itself.")

st.title("你好，我是虚假之镜，梦魇本身。")

st.write("欢迎来到虚假之镜的世界。")
st.write("我是你的私人助理，你的镜像，你的过去，你的未来...")
st.write("愿与你携手走入当下。")

st.caption("今天想聊些什么呢？")

api_key = st.text_input("输入神秘邀请码", type="password")


user_input = st.text_input("请输入你的问题：")

# 判断：只有当用户输入了 API Key 和问题后才执行下面的代码
if user_input and api_key:
    # 创建 DeepSeek 的客户端
    # 注意：base_url 必须设置为 DeepSeek 的官方地址
    client = OpenAI(
        api_key=api_key,                      # 传入刚才输入的 API Key
        base_url="https://api.deepseek.com"   # DeepSeek 的 API 端点
    )

    # 调用 DeepSeek 的对话模型
    # 这行代码会向 DeepSeek 服务器发送请求，并等待回复
    response = client.chat.completions.create(
        model="deepseek-chat",   # 使用的模型名称（deepseek-chat 是 DeepSeek 的对话模型）
        messages=[
            # messages 是一个列表，里面是对话历史
            # 这里我们只发送一条用户消息
            {"role": "user", "content": user_input}
        ]
    )

    # 从返回的 response 中提取 AI 的回答文本
    ai_answer = response.choices[0].message.content

    # 在页面上显示一个分隔线，让界面更清晰
    st.divider()

    # 显示 AI 的回答
    st.write("**‘镜’ 回答：**")
    st.write(ai_answer)

    st.divider()