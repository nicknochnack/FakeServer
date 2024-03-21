from openai import OpenAI

# Streamlit the app framework
import streamlit as st

# Bring the instructor library
import instructor

# Bring in the Base Model class
from pydantic import BaseModel

# Bring in the stock prices function
from stock_data import get_stock_prices

# Create a client
client = OpenAI(api_key="jhjhjh1234", base_url="http://localhost:8000/v1")
# Create a patched client
client = instructor.patch(client=client)


# Structure what want extracted
class ResponseModel(BaseModel):
    ticker: str
    days: int


# The title of the app
st.title("🚀 Fake OpenAI Server App (...llama cpp)")
prompt = st.chat_input("Pass your prompt here")

# If the user types a prompt and hits enter
if prompt:
    st.chat_message("user").markdown(prompt)

    # Function calling LLM call
    response = client.chat.completions.create(
        # which model we want to use
        model="mistral-function-calling",
        # pass through our prompt
        messages=[{"role": "user", "content": prompt}],
        # Add stream
        # stream=True,
        response_model=ResponseModel,
    )

    st.chat_message("ai").markdown(response)

    try:
        prices = get_stock_prices(response.ticker, response.days)
        st.chat_message("ai").markdown(prices)

        # Summary output prompt + prices
        fullresponse = client.chat.completions.create(
            # which model we want to use
            model="mixtral",
            # pass through our prompt
            messages=[{"role": "user", "content": prompt + "\n" + str(prices)}],
            # Add stream
            stream=True,
        )

        with st.chat_message("ai"):
            completed_message = ""
            message = st.empty()
            # Streaming the response out
            for chunk in fullresponse:
                # If the value is not none print it out
                if chunk.choices[0].delta.content is not None:
                    completed_message += chunk.choices[0].delta.content
                    message.markdown(completed_message)
                # print(chunk.choices[0].delta.content, flush=True, end="")

    except Exception as e:
        st.chat_message("ai").markdown("Something went wrong 😭")

    # with st.chat_message("ai"):
    #     completed_message = ""
    #     message = st.empty()
    #     # Streaming the response out
    #     for chunk in response:
    #         # If the value is not none print it out
    #         if chunk.choices[0].delta.content is not None:
    #             completed_message += chunk.choices[0].delta.content
    #             message.markdown(completed_message)
    #         # print(chunk.choices[0].delta.content, flush=True, end="")

# Print it out
# print(response.choices[0].message.content)
