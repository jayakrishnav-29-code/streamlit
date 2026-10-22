
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Visualization")

st.title("Lab 5: Data Visualization")
st.write("Explore data using charts and graphs.")

# Sample data
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [12000, 15000, 10000, 18000, 22000, 25000],
    "Profit": [2000, 3000, 1500, 4000, 5000, 6000]
})

st.subheader("Sales Data")
st.dataframe(data, use_container_width=True)

# Line chart
st.subheader("Monthly Sales Trend")
st.line_chart(data, x="Month", y="Sales")

# Bar chart
st.subheader("Monthly Sales Comparison")
st.bar_chart(data, x="Month", y="Sales")

# Matplotlib chart
st.subheader("Sales and Profit")

fig, ax = plt.subplots()
ax.plot(data["Month"], data["Sales"], marker="o", label="Sales")
ax.plot(data["Month"], data["Profit"], marker="o", label="Profit")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.set_title("Sales vs Profit")
ax.legend()
ax.grid(True)

st.pyplot(fig)
plt.close(fig)

st.success("Charts displayed successfully!")