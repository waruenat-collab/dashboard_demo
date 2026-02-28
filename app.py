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

st.markdown("---")

# ==================================================
# Header Section
# ==================================================
st.title("📊 Sales Dashboard")
st.write("An interactive dashboard for analyzing sales performance.")

st.markdown("---")

# ==================================================
# Data Loading
# ==================================================
df = pd.read_csv("data.csv")

if df.empty:
    st.warning("No data available")
    st.stop()

# ==================================================
# User Controls
# ==================================================
st.subheader("🔧 Select Metric")

metric_options = ["sales", "profit", "customers"]
selected_metric = st.selectbox(
    "Choose a metric to visualize",
    metric_options,
    index=0
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
    title=f"Monthly {selected_metric.capitalize()} Trend",
    markers=True
)

charts["bar"] = px.bar(
    df,
    x="month",
    y=selected_metric,
    title=f"Monthly {selected_metric.capitalize()} Comparison"
)

charts["pie"] = px.pie(
    df,
    values=selected_metric,
    names="month",
    title=f"{selected_metric.capitalize()} Distribution by Month"
)

charts["pie"].update_traces(textinfo="percent+label")

# ==================================================
# Chart Layout
# ==================================================
st.subheader("📈 Data Visualization")

st.caption(
    "The charts below show trends, comparisons, and distribution of the selected metric."
)

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
st.subheader("📋 Raw Data Preview")
st.dataframe(df)

# -----------------------
# End of dashboard application
# -----------------------