import streamlit as st
import pandas as pd
import numpy as np

##title
st.title("welcome")

##display simple text
st.write("this is simple text")

##create a simple dataframe
df=pd.DataFrame({
    'First Column' : [1,2,3,4,5],
    'second column' : [10,20,30,40,50]
})

##display the data frame
st.write("here is the dataframe")
st.write(df)

##create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)