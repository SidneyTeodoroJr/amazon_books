import streamlit as st

def css():
    st.write("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,700;1,300&family=Poppins:wght@200&family=Roboto+Serif:ital,opsz,wght@1,8..144,200&display=swap');

    /*Removing the default menu button*/
    .stDeployButton {
        visibility: hidden;
    } 

    .st-emotion-cache-1vzeuhh {
        background-color: #ffffff;
    }

    /*Styling titles and text*/
    h1 {
        font-size: 2.3em;
        font-family: 'Open Sans', sans-serif;
        color: #5a5959;
    }

    h2 {
        font-size: 1.5em;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 0.5em;
        color: #878787;
    }

    h1, h2 {
        text-align: center;
    }

    h3 {
        font-size: 1.5em;
        text-align: left;
        color: #797777;
    }

    p {
        text-align: justify;
        font-size: 1.2em;
        font-family: 'Roboto Serif', serif;
    }

    #text-home {
        text-align: center;
    }
<style/>
            """, unsafe_allow_html=True)