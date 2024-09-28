import streamlit as st

from predict_page import show_predict_page
from explore_page import show_explore_page
from developers_page import show_developers_page

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Predict", "Explore", "Developers"])

if page == "Predict":
    show_predict_page()
elif page == "Developers":
    show_developers_page()
elif page == "Explore":
    show_explore_page()

