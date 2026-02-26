import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# Page Configuration
# ==================================================
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

# ==================================================
# Header Section
# ==================================================
st.title("📊 Sales Dashboard")
st.write("Interactive dashboard for sales performance analysis")

st.markdown("---")

# ==================================================
# Data Loading
# ==================================================
df = pd.read_csv("data.csv")

# ==================================================
# User Controls
# ==================================================
st.subheader("🔧 Select Metric")

metric_options = ["sales", "profit", "customers"]
selected_metric = st.selectbox(
    "Choose a metric to visualize",
    metric_options
)

st.markdown("---")

# ==================================================
# Chart Generation
# ==================================================
charts = {}

charts["line"] = px.line(
    df,
    x="month",
    y=selected_metric,
    title=f"{selected_metric.capitalize()} Over Time",
    markers=True
)

charts["bar"] = px.bar(
    df,
    x="month",
    y=selected_metric,
    title=f"{selected_metric.capitalize()} Per Month"
)

charts["pie"] = px.pie(
    df,
    values=selected_metric,
    names="month",
    title=f"{selected_metric.capitalize()} Distribution"
)

charts["pie"].update_traces(textinfo="percent+label")

# ==================================================
# Chart Layout
# ==================================================
st.subheader("📈 Data Visualization")

col1, col2, col3 = st.columns(3)

with col1:
    st.plotly_chart(charts["line"], use_container_width=True)

with col2:
    st.plotly_chart(charts["bar"], use_container_width=True)

with col3:
    st.plotly_chart(charts["pie"], use_container_width=True)

# ==================================================
# Data Table
# ==================================================
st.markdown("---")
st.subheader("📋 Raw Data")