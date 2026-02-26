import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

df = pd.read_csv("data.csv")

metric = st.selectbox(
    "Select metric",
    ["sales", "profit", "customers"]
)

line_fig = px.line(
    df,
    x="month",
    y=metric,
    title=f"{metric.capitalize()} Over Time"
)

bar_fig = px.bar(
    df,
    x="month",
    y=metric,
    title=f"{metric.capitalize()} Per Month"
)
st.plotly_chart(bar_fig)

pie_fig = px.pie(
    df,
    values=metric,
    names="month",
    title=f"{metric.capitalize()} Distribution"
)
st.plotly_chart(pie_fig)

pie_fig.update_traces(textinfo="percent+label")

st.plotly_chart(line_fig, use_container_width=True)
st.plotly_chart(bar_fig, use_container_width=True)
st.plotly_chart(pie_fig, use_container_width=True)