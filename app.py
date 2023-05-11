import streamlit as st

if "step1" not in st.session_state:
    st.session_state["step1"] = False
    st.session_state["step2"] = False

def challenge_feedback():
    st.session_state["step1"] = True

def test_callback():
    st.session_state["step2"] = True


st.header("Hello hello, bot or no bot?")

st.button("Test me!", on_click=challenge_feedback)

if st.session_state["step1"]:
    n = int(4861 * 5227 * 5333)
    st.header(f"What is the prime number decomposition of {n} 😏?")
    st.text_input("first prime number")
    st.text_input("second prime number")
    st.button("Go!", on_click=test_callback)

    if st.session_state["step2"]:
        st.header("🚨 WRONG! YOU HUMAN! 🚨")
