import pandas
import streamlit as st
#import pandas #imported with streamlit
from send_email import send_email

st.header('Contact Us')

labels = pandas.read_csv('labels.csv')

with st.form(key='email_forms'):
    user_email = st.text_input("Your email address")
    topic = st.selectbox(label="What topic do you want to discuss?", options=labels)
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: Message from employee page app 

From: {user_email}
Topic: {topic}
{raw_message}"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(user_email, topic, message)
        st.info("Your message was sent! Thank you for contacting us!")
        