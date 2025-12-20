import pandas as pd
import streamlit as st


st.header("Displaying dataframes")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Stu', 'Ian', 'Jamie'],
    'Age': ['24', '27', '31', '21', '35'],
    'City': ['NYC', 'LA', 'Houston', 'Akron', 'Phoenix']
})


st.dataframe(data)