
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Interactive Plotly Dashboard",
    layout="wide"
)

st.title("Lab 9: Interactive Plotly Charts")
st.write("Explore sales data using interactive charts.")

# Sample dataset
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 10000, 18000, 22000, 25000],
    "Profit": [2000, 3000, 1500, 4000, 5000, 6000],
    "Region": ["North", "South", "East", "West", "North", "South"]
})

st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)

# Bar chart
st.subheader("Monthly Sales")
fig_bar = px.bar(
    df,
    x="Month",
    y="Sales",
    color="Region",
    title="Monthly Sales by Region"
)
st.plotly_chart(fig_bar, use_container_width=True)

# Line chart
st.subheader("Sales and Profit Trend")
fig_line = px.line(
    df,
    x="Month",
    y=["Sales", "Profit"],
    markers=True,
    title="Sales vs Profit"
)
st.plotly_chart(fig_line, use_container_width=True)

# Pie chart
st.subheader("Sales Distribution")
fig_pie = px.pie(
    df,
    names="Region",
    values="Sales",
    title="Sales Share by Region"
)
st.plotly_chart(fig_pie, use_container_width=True)

st.success("Interactive Plotly dashboard loaded!")