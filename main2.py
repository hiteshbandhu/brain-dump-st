import openai
import streamlit as st
import os
openai.api_key = st.secrets["pass"]

st.set_page_config(page_title="Organise, Dump & Laugh(Cry)")
st.header("DUMP YOUR BRAIN 🧠 - Made by Hitesh Bandhu" )

mode = st.radio("Mode", ["Standard", "Dreamy", "Sarcastic", "Truth Bombs - Roast the hell out of me" ])


prompt_system = f""" I want to you to take in input as Brain Dump of a user, which consists of what he is thinking and structure the work and organise it into tasks, basically provide clarity and organization. Break Task into Bullet Points and if required, break them into smaller subtopics.Also, provide a paragraph of witty commentary on the dump,  Keep the tone {mode} and adhere to it properly- include punchlines wherever nexessary, keep it concise, properly implement the tone.  Don't Output any Explanations, Never Output anything not required. keep output in the format :

```Tasks```
```Commentary in Specified Tone```


"""

user_input = st.text_area("Dump all here : ")

prompt_user = f""" Use the following Format : {mode}, Brain Dump = {user_input}"""


def code_gen(temperature=0.6):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": prompt_user},
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content


if st.button("Organize") :
    with st.spinner("Generating"):
        response = code_gen()
        st.success("Done !")

    st.text_area("Organized Dump !", response, height=600)





# watch fluffy and trevor noah wih nfs, also go to a movie with lenskart, then do dinner together. I was reading a book, dont know what to do about it, shit i also wanted to write my newsletter.
