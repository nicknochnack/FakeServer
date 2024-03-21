from openai import OpenAI
import streamlit as st

import instructor
from pydantic import BaseModel

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="123",
)

# Enables `response_model`
client = instructor.patch(client=client)


class UserDetail(BaseModel):
    stock_ticker: str
    start_date: int
    end_date: str


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
        max_tokens=-1,
        model="mistral-function-calling",
        response_model=UserDetail,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    complete_response = ""
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        for chunk in response:
            st.write(chunk)

    st.session_state.messages.append(
        {"role": "assistant", "content": complete_response}
    )
