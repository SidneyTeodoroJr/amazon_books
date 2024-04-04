# Importing dependencies
import pandas as pd
import streamlit as st
import plotly.express as px

# APP page settings
st.set_page_config(
    layout="wide",
    menu_items={
    'Get Help': 'https://github.com/SidneyTeodoroJr',
    'Report a bug': "https://github.com/SidneyTeodoroJr/amazon_books",
    'About': "Contributions are welcome!"
    }
)

# Importing the CSS
# with open("app\modules\style.css") as css:
#     st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.write(f"<H1>📖 Top-100 Trending Books</H1>", unsafe_allow_html=True)
st.write(f'<p id="text-home">This project presents data from 100 most popular books along with customer reviews.</p>', unsafe_allow_html=True)

# Reading the files
df_reviews = pd.read_csv("app\datasets\customer reviews.csv")
df_top100_books = pd.read_csv("app\datasets\Top-100 Trending Books.csv")

# Performing the calculations
price_max = df_top100_books["book price"].max()
price_min = df_top100_books["book price"].min()

max_price = st.sidebar.slider("💵 Price Range:", price_min, price_max, price_max) # Controle deslizante
df_books = df_top100_books[df_top100_books["book price"] <= max_price] # Filtrando os livros 
st.dataframe(df_books, height=400, use_container_width=True)

# Displaying the graphs
def graphic(df_books):
    fig1 = px.bar(df_books["year of publication"].value_counts())
    fig2 = px.histogram(df_books["book price"])

    tab1, tab2 = st.tabs(["YEAR OF PUBLICATION", "BOOK PRICE"])
    with tab1:
        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

    with tab2:
        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

graphic(df_books)