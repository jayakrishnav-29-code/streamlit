
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("Lab 10: Interactive Sales Dashboard")
st.write("Analyze sales by month, region, and product.")

# Sample dataset
df = pd.DataFrame({
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jan", "Feb", "Mar", "Apr", "May", "Jun"
    ],
    "Region": [
        "North", "South", "East", "West",
        "North", "South", "East", "West",
        "North", "South", "East", "West"
    ],
    "Product": [
        "Laptop", "Mobile", "Tablet", "Laptop",
        "Mobile", "Tablet", "Laptop", "Mobile",
        "Tablet", "Laptop", "Mobile", "Tablet"
    ],
    "Sales": [
        12000, 15000, 10000, 18000,
        22000, 25000, 14000, 17000,
        11000, 20000, 24000, 16000
    ]
})

# Sidebar filters
st.sidebar.header("Dashboard Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=list(df["Region"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    df["Product"].unique(),
    default=list(df["Product"].unique())
)

filtered_df = df[
    df["Region"].isin(regions)
    & df["Product"].isin(products)
]

# Summary cards
total_sales = filtered_df["Sales"].sum()
total_records = len(filtered_df)
average_sales = (
    filtered_df["Sales"].mean()
    if total_records > 0 else 0
)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,}")
col2.metric("Average Sales", f"₹{average_sales:,.0f}")
col3.metric("Records", total_records)

# Display filtered data
st.subheader("Sales Records")
st.dataframe(filtered_df, use_container_width=True)

# Sales by month
if not filtered_df.empty:
    monthly = (
        filtered_df.groupby("Month", as_index=False)["Sales"]
        .sum()
    )

    month_order = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun"
    ]

    monthly["Month"] = pd.Categorical(
        monthly["Month"],
        categories=month_order,
        ordered=True
    )
    monthly = monthly.sort_values("Month")

    fig = px.bar(
        monthly,
        x="Month",
        y="Sales",
        title="Monthly Sales",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

    # Sales by region
    region_sales = (
        filtered_df.groupby("Region", as_index=False)["Sales"]
        .sum()
    )

    fig2 = px.pie(
        region_sales,
        names="Region",
        values="Sales",
        title="Sales by Region"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No records match your selected filters.")

st.success("Sales dashboard loaded successfully!")