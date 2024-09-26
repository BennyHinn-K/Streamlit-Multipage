import streamlit as st

from forms.contacts import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()
# Header section
col1,col2 = st.columns(2, gap="small", vertical_alignment="center")

# --- Columns Sections--
with col1:
    st.image("Brains.jpg",)

with col2:
    st.header("Hello I'm BennyHinn Kariuki.")
    if st.button(" 📞 Contact Me"):
        show_contact_form()
      
with st.container():
    st.title("I am a passionate Streamlit Developer")
    st.write("##### My eyes are caught by  solving problems and easy data collection and presentation using Python and Streamlit framework.")
    st.link_button("[Learn more 📖:]",url ="http://bennyhinn-kariuki.kesug.com/index.html?i=1")




st.write(''' As a seasoned professional in the Streamlit framework and Python programming, I have honed my expertise in developing interactive, data-driven applications that streamline complex workflows and enhance user engagement. My extensive experience with Streamlit enables me to design and deploy intuitive dashboards and real-time data visualizations with ease, leveraging Python’s robust libraries to create scalable solutions. I excel in integrating diverse data sources, optimizing performance, and implementing advanced features that transform raw data into actionable insights. My commitment to best practices and continuous learning ensures that my projects not only meet but exceed industry standards, delivering high-quality, user-centric applications that drive informed decision-making and operational efficiency.''')
  
st.header("Other Skills:")
st.write("##### . Kotlin Programming ")
st.write("##### . Jetpack Compose")
st.write("##### . Web Development")
st.write("##### . Web  Design")


