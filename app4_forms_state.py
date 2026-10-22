
import streamlit as st

st.set_page_config(page_title="Forms and Session State")

st.title("Lab 4: Forms and Session State")

# Initialize session state
if "count" not in st.session_state:
    st.session_state.count = 0

# Form
st.subheader("Student Registration")

with st.form("student_form"):
    name = st.text_input("Student Name")
    email = st.text_input("Email Address")
    course = st.selectbox(
        "Select Course",
        ["Python", "Streamlit", "Data Science", "Web Development"]
    )

    submitted = st.form_submit_button("Register")

if submitted:
    if name.strip() and email.strip():
        st.success("Registration successful!")
        st.write("Name:", name)
        st.write("Email:", email)
        st.write("Course:", course)
    else:
        st.error("Please enter your name and email.")

# Session state counter
st.divider()
st.subheader("Counter using Session State")

st.write("Current count:", st.session_state.count)

col1, col2 = st.columns(2)

with col1:
    if st.button("Increment"):
        st.session_state.count += 1

with col2:
    if st.button("Reset"):
        st.session_state.count = 0