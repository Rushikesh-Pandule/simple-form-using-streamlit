import streamlit as st
import pandas as pd

st.title("text input")

name=st.text_input("enter your name")

age=st.slider("select age:",0,100,25)
st.write(f"YOUR AGE IS :{age}.")

options = ["Python","Java","C++","JavaScript"] 
choice = st.selectbox("Choose your favorite language:",options) 

st.write(f"You selected {choice}.")

if name:
    st.write(f"hello,{name}")

data = {
    "Age": [10, 20, 30,],
    "Name": ["Alice", "Bob", "Charlie"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("choose file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)