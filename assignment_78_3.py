import streamlit as st

st.title("Simple Interest Calculator")

P = st.number_input("Enter Principal Amount", value=0.0)
R = st.number_input("Enter Rate of Interest", value=0.0)
T = st.number_input("Enter Time Period", value=0.0)

if st.button("Calculate"):
    SI = (P * R * T) / 100
    st.success(f"Simple Interest is : {SI}")
