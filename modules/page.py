import streamlit as st

# APP page settings
def page():
    st.set_page_config(
        page_title="Top-100 Trending Books", 
        page_icon="app\icon\icon.png", 
        layout="wide",
        initial_sidebar_state="auto", 
        menu_items={
            'Get Help': 'https://github.com/SidneyTeodoroJr',
            'Report a bug': "https://github.com/SidneyTeodoroJr/amazon_books",
            'About': "Contributions are welcome!"
        }
    )