import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

df = pd.read_csv("data.csv")

fig = px.line(df, x="month", y="sales")
st.plotly_chart(fig)