import streamlit as st
from groq import Groq

# --------------------------------
# GROQ API CLIENT
# --------------------------------
client = Groq(
    api_key=st.secrets["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"]
)

# --------------------------------
# PAGE TITLE
# --------------------------------
st.title("🤖 HIM AI HR Mentor")

st.write("Ask any HRM question.")

# --------------------------------
# USER INPUT
# --------------------------------
question = st.text_input("Enter Question")

# --------------------------------
# AI RESPONSE
# --------------------------------
if question:

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f'''
                You are an HRM expert.

                Answer professionally with:
                - Definitions
                - Examples
                - HR insights
                - MBA-level explanation

                Question:
                {question}
                '''
            }
        ],
        model="llama-3.1-8b-instant",
    )

    st.write(completion.choices[0].message.content)
