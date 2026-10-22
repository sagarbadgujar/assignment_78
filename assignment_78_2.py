import streamlit as st

st.title("Even or Odd Number")

No = st.number_input("Enter Number", value=0, step=1)

if st.button("Check"):
    if No % 2 == 0:
        st.success("Number is Even")
    else:
        st.success("Number is Odd")
