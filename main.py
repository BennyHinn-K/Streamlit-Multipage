import  streamlit as st 


about_page = st.Page(
    page="pages/About.py",
    title= "About Me ",
    icon= "😊",
    default= True,
)

project1_page = st.Page(
    page="pages/ChatBot.py",
    title= "ChatBot",
)

project2_page = st.Page(
    page="pages/Sales_Dashboard.py",
    title="Sales Dashboard",
)   

# creating the navigation sections
pg = st.navigation(
    {
        "info":[about_page],
        "projects": [project1_page,project2_page],
    }
)
# running the navigation
pg.run()

# -- images shared by all pages--.
st.logo= ("Brains.jpg")