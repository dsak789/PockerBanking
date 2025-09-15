from streamlit_cookies_manager import EncryptedCookieManager
import streamlit as st

cookies = EncryptedCookieManager(prefix="pb_auth",password="pb_auth_789")
if not cookies.ready():
    st.stop()

class PBAuthentication:
    def __init__(self):
        if "loginid" not in st.session_state:
            st.session_state.loginid = cookies.get("loginid")

        if st.session_state.loginid:
            st.success(f"logged in as {st.session_state.loginid}")

        else:
            self.login()

    def login(self):
        loginid = st.text_input("Enter loginID:")
        loginpwd = st.text_input("Enter Password:",type="password")
        loginbtn = st.button("LOGIN")

        if loginbtn:
            if loginid and loginpwd :
                st.session_state.loginid = loginid
                cookies["loginid"] = loginid
                cookies.save()
                st.success(f"Logged in as {loginid}")
            else:
                st.error("enter credentials")