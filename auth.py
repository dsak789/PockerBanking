from streamlit_cookies_manager import EncryptedCookieManager
from dbDao import AuthennticationDAO 
import streamlit as st
import asyncio 

cookies = EncryptedCookieManager(prefix="pb_auth",password="pb_auth_789")
if not cookies.ready():
    st.stop()

class PBAuthentication:
    def __init__(self):
        print("hello",cookies.get("userid"))
        self.authDao = AuthennticationDAO()
        if "userid" not in st.session_state and cookies.get('userid'):
                st.session_state.userid = cookies.get("userid")
            

        if "name" not in st.session_state and cookies.get('name'):
                st.session_state.name = cookies.get("name")
           

    def loginCheck(self):  
        if st.session_state.userid and st.session_state.name:
            st.success(f"logged in as {st.session_state.name}")
            print("sessions: ",st.session_state)
            if st.button("Logout"):
                st.session_state.pop("userid",None)
                st.session_state.pop("name",None)
                print("Clear Session- ",st.session_state.clear())
                if "userid" in cookies:
                    del cookies['userid']
                if "name" in cookies:
                    del cookies['name']
                cookies['userid'] = ""
                cookies['name'] = ""
                cookies.clear()
                st.success("Logged out Successfully.")
                st.rerun()
                return 
            return True
        else:
            tab1,tab2 = st.tabs(["Signin","Signup"])
            with tab1:
                self.loginUI()
            with tab2:
                self.registerUI()


    def loginUI(self):
        loginid = st.text_input("Enter loginID:")
        loginpwd = st.text_input("Enter Password:",type="password")
        loginbtn = st.button("LOGIN")

        if loginbtn:
            if loginid and loginpwd :
                payload={
                    "userid":loginid,
                    "password":loginpwd
                }
                res = asyncio.run(self.authDao.login(userLoginData=payload))
                print(f"login: {res}")
                if res['success']:
                    st.session_state.userid = res['userid']
                    st.session_state.name = res['name']
                    cookies["userid"] = res['userid']
                    cookies["name"] =res['name']
                    cookies.save()
                    st.success(f"Logged in as {res['userid']} - {res['name']}")
                    st.rerun()
                    return
                else:
                    st.error(f"{res['msg']}")
                    return
            else:
                st.warning("Enter credentials")
                return
    
    def registerUI(self):
        st.header("Register")
        name = st.text_input("Enter name") 
        phone = st.text_input("Enter Phone No.")
        userid = st.text_input("Enter UserId")
        password = st.text_input("Enter Password")
        cnfpwd = st.text_input("Enter Confirm Password")
        regiBtn = st.button("REGISTER")

        if regiBtn:
            if name and phone and userid and password and cnfpwd:
                if not phone.isdigit():
                    st.warning("Phone number must be digits only")
                    return
                if len(phone) < 10:
                    st.warning("Phone number should be 10 digits")
                    return

                if password == cnfpwd:
                    userRegiData={
                        "name":name,
                        "phoneno":phone,
                        "userid":userid,
                        "password":cnfpwd,
                        "role":"player"
                        }
                    res = asyncio.run(self.authDao.register(userRegiData=userRegiData))
                    print(f"regi: {res}")
                    if res['success']:
                        st.success(f"Registeration Done with UserID: {userid}")
                        st.rerun()
                        return
                    else:
                        st.warning(f"{res}")
                else:
                    st.error("Password missmatch..!")
            else:
                st.warning("All Fields required..!")

