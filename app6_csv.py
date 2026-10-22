
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Data Analyzer")

st.title("Lab 6: File Upload and Pandas")
st.write("Upload a CSV file to explore and analyze your data.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("CSV file uploaded successfully!")

        st.subheader("Dataset Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Dataset Information")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Rows", df.shape[0])

        with col2:
            st.metric("Total Columns", df.shape[1])

        st.subheader("Column Names")
        st.write(list(df.columns))

        st.subheader("Summary Statistics")
        st.write(df.describe(include="all"))

        st.subheader("Missing Values")
        st.write(df.isnull().sum())

        st.subheader("Download Processed Data")
        csv_data = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="processed_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"Could not read the CSV file: {e}")

else:
    st.info("Upload a CSV file to begin.")