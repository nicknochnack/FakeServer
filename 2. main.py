from openai import OpenAI
import streamlit as st

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="123",
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": """You are a helpful assistant. If you do not know the answer, reply I don't know 
                don't make things up.""",
        }
    ]

st.title("🚀 LLaMa CPP Python")
for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Pass your input here")
if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="llama.cpp/models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf",
        messages=st.session_state.messages,
        stream=True,
    )

    complete_response = ""
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                complete_response += chunk.choices[0].delta.content
                message_placeholder.markdown(complete_response + "▌")
                message_placeholder.markdown(complete_response)
    st.session_state.messages.append(
        {"role": "assistant", "content": complete_response}
    )
