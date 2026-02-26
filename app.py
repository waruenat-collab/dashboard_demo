import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

df = pd.read_csv("data.csv")
st.dataframe(df)