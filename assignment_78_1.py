import streamlit as st

st.title("Addition of Two Numbers")

No1 = st.number_input("Enter First Number", value=0)
No2 = st.number_input("Enter Second Number", value=0)

if st.button("Add"):
    Ans = No1 + No2
    st.success(f"Addition is : {Ans}")
