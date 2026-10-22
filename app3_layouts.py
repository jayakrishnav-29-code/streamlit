
import streamlit as st

st.set_page_config(
    page_title="Layouts Demo",
    page_icon="📊",
    layout="wide"
)

st.title("Lab 3: Streamlit Layouts")
st.write("Learn to organize content using layouts.")

# Sidebar
st.sidebar.header("Settings")
theme = st.sidebar.selectbox(
    "Choose Theme",
    ["Light", "Dark"]
)
font_size = st.sidebar.slider(
    "Font Size",
    10, 30, 15
)

st.sidebar.write("Selected theme:", theme)
st.sidebar.write("Selected font size:", font_size)

# Two columns
st.subheader("Columns")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Sales", "₹25,000")

with col2:
    st.metric("Customers", "1,200")

# Tabs
st.subheader("Tabs")

tab1, tab2, tab3 = st.tabs(
    ["Overview", "Analysis", "About"]
)

with tab1:
    st.write("This is the Overview section.")

with tab2:
    st.write("This is the Analysis section.")

with tab3:
    st.write("This app demonstrates Streamlit layouts.")

# Container
st.subheader("Container")

with st.container():
    st.write("Grouped Section")
    st.write("These elements are inside one container.")

# Expander
with st.expander("Show More Details"):
    st.write("This content appears when you expand this section.")