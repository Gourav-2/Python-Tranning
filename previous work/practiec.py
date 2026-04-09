# for i in range(0,11):
    # print("2 * " ,   i , "=", (i*2))
# 
# a =input("Enter your name: ")
# b = a[::-1]
# if (a==b):
    # print("pelendrom")
# else:
    # print("not pelendrom")

import streamlit as st 
st.title("my first streamlit app")
name = st.text_input("enter your name")
st.write("hello", name)
