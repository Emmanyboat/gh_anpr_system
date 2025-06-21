from supabase import create_client
import streamlit as st

url = st.secrets["https://ozjfvcfkhuajljlfdjio.supabase.co"]
key = st.secrets["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im96amZ2Y2ZraHVhamxqbGZkamlvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTAxOTQ0NzUsImV4cCI6MjA2NTc3MDQ3NX0.7QBEW-65dDzTWcKxvtCVg7tVfRCRorDWCWPDsamRy3E  "]
supabase = create_client(url, key)

if "user" not in st.session_state:
    st.session_state.user = None

def login(email, password):
    result = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if result.user:
        st.session_state.user = result.user
        st.success("Logged in")
    else:
        st.error("Failed login")

# Login form
if not st.session_state.user:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        login(email, password)
    st.stop()

def get_user_role(user_id):
    response = supabase.table("app_users").select("role").eq("id", user_id).execute()
    return response.data[0]["role"] if response.data else None
def show_admin_dashboard():
    st.write("Welcome to the Admin Dashboard!")

def show_police_officer_dashboard():
    st.write("Welcome to the Police Officer Dashboard!")

role = None
if st.session_state.user:
    role = get_user_role(st.session_state.user.id)

if role == "admin":
    show_admin_dashboard()
elif role == "police_officer":
    show_police_officer_dashboard()