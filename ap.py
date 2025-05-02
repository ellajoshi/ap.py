import streamlit as st
st.title("hello world")
name=st.text_input("enter your name")
age=int(st.text_input("enter your age"))
if age>15 and age<=18:
  st.write("welcome"+name,age,"you are a teen age kid")
elif age<=15:
  st.write("welcome"+name,age,"you are a  kid")
