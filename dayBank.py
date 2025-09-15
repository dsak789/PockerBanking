import streamlit as st
class DayBank:
    def __init__(self,date):
        st.set_page_config(
            page_title="Day Banking Statement",
            page_icon="💸",
            layout="wide",
            initial_sidebar_state="auto"
        )
        self.date = date

        st.header("Pocker-Uno-Bluff")
        self.start()


    def pbheader(self):
        st.header("Pocker Day Statement")


    def start(self):
        if(st.button("Start Game")):
            self.pbheader()