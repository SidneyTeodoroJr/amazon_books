import streamlit as st

from home import df_reviews, df_top100_books
from modules.page import *

page()

with open("modules\style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

books = df_top100_books["book title"].unique() # Single list of titles
book = st.sidebar.selectbox("📖 Select a book:", books, index=5) # Menu

# Filtering
df_book = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.write(f"<H1>📘{book_title}</H1>", unsafe_allow_html=True)
st.write(f"<h2>{book_genre}</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of publication", book_year)

st.divider() # Line

# Iterating over evaluations
for row in df_reviews_f.values:
    message = st.chat_message("📙")
    message.write(f"<h3>{row[2]}</h3>", unsafe_allow_html=True)
    message.write(f"<p>{row[5]}</p>", unsafe_allow_html=True)