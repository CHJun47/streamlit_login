import streamlit as st
import st_login_form as slf
# from st_login_form import login_form

client = slf.login_form()

if st.session_state["authenticated"]:
    if st.session_state["username"]:
        st.success(f"Welcome {st.session_state['username']}")
    else:
        st.success("Welcome guest")
else:
    st.error("Not authenticated")