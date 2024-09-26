import streamlit as st

WEBHOOK_URL="https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZkMDYzMDA0Mzc1MjZiNTUzNzUxMzEi_pc"
import re
import requests

#  Chatgpt regex pattern
# Basic regex pattern for email validation
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    return re.match(email_pattern, email) is not None


def contact_form():
    with st.form("Enter your Details"):
            firstName = st.text_input("Enter your firstname :"),
            lastName = st.text_input("Enter your lastname :") ,
            contact = st.text_input("Enter your contacts :",placeholder="+254........"),  
            email = st.text_input("Enter Your Email Address.",placeholder="abcd@gmail.com")
            st.form_submit_button("Submit Details")

            if st.form_submit_button: 
                if not WEBHOOK_URL:
                    st.error(" Email service is not set up. Please try later", icon="📧")
                    st.stop()
                if not firstName : 
                    st.error(" Please provide your firstname.", icon="🧑🏾")
                    st.stop()
                if not lastName: 
                    st.error(" Please provide your lastname.", icon="🧑🏾")
                    st.stop()
                if not contact: 
                    st.error(" Please provide your Contacts.", icon="📞")
                    st.stop()
                if not email: 
                    st.error(" Please provide your email.", icon="📧")
                    st.stop()
                if not is_valid_email(email): 
                    st.error(" Please provide a valid email address.", icon="📧")
                    st.stop()

                data = {"email":email,"firstname":firstName ,"lastname":lastName ,"contact":contact,}
                response = requests.post(WEBHOOK_URL, json=data)

                if response.status_code == 200:
                    st.success(" Your details have been successfully sent !", icon="📩")
                else:
                    st.error("There was an error sending your details.",icon="❌")                    
    
   
