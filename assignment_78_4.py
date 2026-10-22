
import streamlit as st

st.title("Student Result Calculator")

Name = st.text_input("Enter Student Name")

M1 = st.number_input("Enter Subject 1 Marks", min_value=0, max_value=100, step=1)
M2 = st.number_input("Enter Subject 2 Marks", min_value=0, max_value=100, step=1)
M3 = st.number_input("Enter Subject 3 Marks", min_value=0, max_value=100, step=1)

if st.button("Calculate"):
    Total = M1 + M2 + M3
    Percentage = (Total / 300) * 100

    st.write("Student Name :", Name)
    st.write("Total Marks :", Total)
    st.write("Percentage :", round(Percentage, 2))

    if M1 >= 40 and M2 >= 40 and M3 >= 40:
        st.success("Result : Pass")
    else:
        st.error("Result : Fail")
