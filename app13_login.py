import streamlit as st
import psycopg2
import hashlib
import hmac

st.set_page_config(
    page_title="Login and Signup",
    page_icon="🔐"
)

st.title("🔐 Login / Signup System")


def get_connection():
    config = st.secrets["postgres"]

    return psycopg2.connect(
        host=config["host"],
        port=config["port"],
        dbname=config["database"],
        user=config["user"],
        password=config["password"]
    )


def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def signup(username, password):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO users (username, password_hash)
                VALUES (%s, %s)
                ON CONFLICT (username) DO NOTHING
                RETURNING id
                """,
                (username, hash_password(password))
            )

            created_user = cursor.fetchone()
            connection.commit()

            return created_user is not None

    finally:
        connection.close()


def login(username, password):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT password_hash
                FROM users
                WHERE username = %s
                """,
                (username,)
            )

            result = cursor.fetchone()

            if result is None:
                return False

            entered_hash = hash_password(password)

            return hmac.compare_digest(
                result[0],
                entered_hash
            )

    finally:
        connection.close()


tab_signup, tab_login = st.tabs(["Sign Up", "Login"])

with tab_signup:
    st.subheader("Create an Account")

    new_username = st.text_input(
        "Choose a username",
        key="signup_username"
    )

    new_password = st.text_input(
        "Choose a password",
        type="password",
        key="signup_password"
    )

    confirm_password = st.text_input(
        "Confirm password",
        type="password",
        key="confirm_password"
    )

    if st.button("Create Account"):
        if not new_username.strip() or not new_password:
            st.error("Enter a username and password.")

        elif new_password != confirm_password:
            st.error("Passwords do not match.")

        elif len(new_password) < 8:
            st.error("Use a password with at least 8 characters.")

        else:
            try:
                created = signup(
                    new_username.strip(),
                    new_password
                )

                if created:
                    st.success("Account created successfully!")
                else:
                    st.error("That username already exists.")

            except psycopg2.Error:
                st.error(
                    "Database operation failed. "
                    "Check your database connection and table."
                )

with tab_login:
    st.subheader("Login to Your Account")

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):
        if not username.strip() or not password:
            st.error("Enter your username and password.")

        else:
            try:
                if login(username.strip(), password):
                    st.success(
                        f"Welcome, {username.strip()}!"
                    )
                else:
                    st.error("Invalid username or password.")

            except psycopg2.Error:
                st.error(
                    "Database operation failed. "
                    "Check your PostgreSQL connection."
                )

st.caption("Lab 13: Streamlit + PostgreSQL")