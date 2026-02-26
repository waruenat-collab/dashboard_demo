import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("📊 Sales Dashboard")
st.write("Interactive dashboard for sales performance analysis")

# เส้นคั่นหลัง header
st.markdown("---")

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("data.csv")

# -----------------------------
# Metric Selector
# -----------------------------
st.subheader("🔧 Select Metric")

metric = st.selectbox(
    "Choose a metric to visualize",
    ["sales", "profit", "customers"]
)

# เส้นคั่นก่อนกราฟ
st.markdown("---")

# -----------------------------
# Charts
# -----------------------------
st.subheader("📈 Data Visualization")

col1, col2, col3 = st.columns(3)

# Line Chart
with col1:
    line_fig = px.line(
        df,
        x="month",
        y=metric,
        title=f"{metric.capitalize()} Over Time",
        markers=True
    )
    st.plotly_chart(line_fig, use_container_width=True)

# Bar Chart
with col2:
    bar_fig = px.bar(
        df,
        x="month",
        y=metric,
        title=f"{metric.capitalize()} Per Month"
    )
    st.plotly_chart(bar_fig, use_container_width=True)

# Pie Chart
with col3:
    pie_fig = px.pie(
        df,
        values=metric,
        names="month",
        title=f"{metric.capitalize()} Distribution"
    )
    pie_fig.update_traces(textinfo="percent+label")
    st.plotly_chart(pie_fig, use_container_width=True)

# -----------------------------
# Data Table
# -----------------------------
st.markdown("---")
st.subheader("📋 Raw Data")