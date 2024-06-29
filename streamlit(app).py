import streamlit as st
import time as t
#to create an image
st.image("https://images.app.goo.gl/U43NUtgAzQ3gzZgr6")

#title - used to add the title of an app
st.title("Streamlit App")
#header -
st.header("Machine Learning")
#subheader -
st.subheader("Algorithms")
#information message
st.info("Information details of the app")
#warning message
st.warning("Warning message")
#write function also used to write code
st.write("Streamlit is a python library used to create web apps")
st.write("range(50)")
st.write(range(50))  #without comma
#error message
st.error("Error message")
#success message
st.success("Success message")
#markdown
st.markdown("# Streamlit App")
st.markdown("## Streamlit App")
st.markdown("### Streamlit App")
st.markdown(" :moon:")
st.markdown("**Streamlit App**")
st.markdown(" :apple:")
#text
st.text("Streamlit is a python library used to create web apps")
#to write a caption
st.caption("caption is here")
#to display mathematical equation
st.latex(r''' a+b x^2+c''')

#widget
st.checkbox("login")
st.button("Submit")
st.radio("Select",["A","B","C"])
st.selectbox("Select",["A","B","C"])
st.multiselect("Select",["A","B","C"])
st.select_slider("Rating",["bad","good","excellent"])
st.slider("Select",1,10)
#number input
st.number_input("Enter a number")
#text input
st.text_input("Enter your email")
#date_input
st.date_input("Enter your date of birth")
#time_input
st.time_input("what time is it?")
#text area
st.text_area("Enter your message")

#file uploader
st.file_uploader("Upload a file")
#color picker
st.color_picker("Choose a color")
#progress bar
st.progress(50)
#spinner shows temporary waiting message
with st.spinner("In progress"):
    t.sleep(2)
    st.success("Done")
 #balloons display balloons for celebration
st.balloons()

#side bar pin elements to the left side bar
st.sidebar.title("This is a side bar")
st.sidebar.text_input("mail address")
st.sidebar.text_input("password")
st.sidebar.button("click")
st.sidebar.radio("Select",["1","2","3"])

#data visualization
import pandas as pd
import numpy as np

st.title("bar chart")
data = pd.DataFrame(np.random.randn(50,2),columns=["a","b"])
st.bar_chart(data)

st.title("line chart")
st.line_chart(data)

st.title("area chart")
st.area_chart(data)































