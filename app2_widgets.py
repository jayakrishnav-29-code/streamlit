import streamlit as st
from datetime import date

# Page title
st.set_page_config(
    page_title="Widgets Playground",
    page_icon="🧪",
    layout="centered"
)

st.title("Widgets Playground")
st.write("Explore the different Streamlit widgets below.")

st.divider()

# 1. Text input
name = st.text_input("Enter your name")

# 2. Number input
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=20
)

# 3. Slider
marks = st.slider(
    "Select your marks",
    min_value=0,
    max_value=100,
    value=75
)

# 4. Dropdown
city = st.selectbox(
    "Select your city",
    ["Bengaluru", "Hyderabad", "Chennai", "Mumbai", "Delhi"]
)

# 5. Multiselect
skills = st.multiselect(
    "Select your skills",
    ["Python", "Streamlit", "SQL", "Machine Learning", "Pandas"]
)

# 6. Radio buttons
gender = st.radio(
    "Select your gender",
    ["Male", "Female", "Other", "Prefer not to say"]
)

# 7. Checkbox
agree = st.checkbox("I agree to the terms")

# 8. Date input
dob = st.date_input(
    "Select your date of birth",
    value=date(2000, 1, 1)
)

# 9. File uploader
uploaded_file = st.file_uploader(
    "Upload a file",
    type=["csv", "txt", "pdf", "png", "jpg"]
)

st.divider()

# 10. Submit button
if st.button("Submit"):
    st.subheader("Your Submitted Details")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Gender:", gender)
    st.write("Agreed to terms:", agree)
    st.write("Date of birth:", dob)

    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
    else:
        st.info("No file uploaded.")

    st.success("Form submitted successfully!")