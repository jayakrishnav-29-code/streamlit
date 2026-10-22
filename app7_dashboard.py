
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Lab 7: Interactive Sales Dashboard")
st.write("Analyze sales using interactive filters and charts.")

# Create sample sales data
np.random.seed(42)

dates = pd.date_range(
    start="2026-01-01",
    periods=60,
    freq="D"
)

products = ["Laptop", "Mobile", "Tablet", "Headphones"]
regions = ["North", "South", "East", "West"]

df = pd.DataFrame({
    "Date": dates,
    "Product": np.random.choice(products, 60),
    "Region": np.random.choice(regions, 60),
    "Sales": np.random.randint(1000, 15000, 60),
    "Quantity": np.random.randint(1, 20, 60)
})

# Calculate revenue
df["Revenue"] = df["Sales"] * df["Quantity"]

# Sidebar filters
st.sidebar.header("Dashboard Filters")

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

selected_products = st.sidebar.multiselect(
    "Select Product",
    products,
    default=products
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=dates.min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=dates.max().date()
)

# Filter data
filtered_df = df[
    df["Region"].isin(selected_regions)
    & df["Product"].isin(selected_products)
    & (df["Date"].dt.date >= start_date)
    & (df["Date"].dt.date <= end_date)
]

st.subheader("Sales Summary")

if filtered_df.empty:
    st.warning("No sales data matches these filters.")
else:
    total_sales = filtered_df["Sales"].sum()
    total_revenue = filtered_df["Revenue"].sum()
    total_quantity = filtered_df["Quantity"].sum()
    average_sales = filtered_df["Sales"].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Sales", f"{total_sales:,.0f}")
    col2.metric("Total Revenue", f"₹{total_revenue:,.0f}")
    col3.metric("Quantity Sold", f"{total_quantity:,}")
    col4.metric("Average Sale", f"{average_sales:,.0f}")

    # Sales by product
    st.subheader("Sales by Product")

    product_sales = (
        filtered_df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(product_sales)

    # Sales by region
    st.subheader("Sales by Region")

    region_sales = (
        filtered_df.groupby("Region")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(region_sales)

    # Daily sales trend
    st.subheader("Daily Sales Trend")

    daily_sales = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .sort_index()
    )

    st.line_chart(daily_sales)

    # Filtered records
    st.subheader("Sales Records")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    # Download filtered data
    csv_data = filtered_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Filtered Sales Data",
        data=csv_data,
        file_name="filtered_sales.csv",
        mime="text/csv"
    )

st.success("Interactive dashboard loaded.")