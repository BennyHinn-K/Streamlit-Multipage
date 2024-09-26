import streamlit as st
 


st.title("Simple Login Application")

menu = [ "Homepage","Signup","Login"]
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Home":
        st.subheader("Home")

elif choice == "Login":
    st.write("## Login into your account. ")

    username = st.text_input("Enter your Username.")
    password = st.text_input("Enter your password.",type="password")
    

if st.sidebar.checkbox("Login"):
        st.success("Successfully Logged in as {}".format(username))
            
        task  = st.selectbox("Tasks",["Add a New post","Analytics","Profiles"])
        if task == "Add a New post":
            st.subheader("Add a New post")

        elif task == "Analytics":
            st.subheader("Analytics")

        elif task == ("Profiles"):
            st.subheader(" User Profiles ")    
 

if choice == "Signup":
        st.subheader("Create a new account")
        new_FirstName = st.text_input(" Enter your first name")
        new_LastName  = st.text_input(" Enter your last name")
        new_Email = st.text_input(" Enter your email" , type= "default")
        new_username = st.text_input(" Enter your new username")
        if st.checkbox("SignUp"):
            st.success("Successfully SignedUp in as {}".format(username))
 


            
      





