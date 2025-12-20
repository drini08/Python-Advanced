import streamlit as st

tab1, tab2, tab3 = st.tabs(['Tab1', 'Tab2', 'Tab3'])

with tab1:
    st.header("Content for Tab 1")
    st.write("This is the content of Tab 1")

with tab2:
    st.header("Content for Tab 2")
    st.write("This is the content of Tab 2")

with tab3:
    st.header("Content for Tab 3")
    st.write("This is the content of Tab 3")