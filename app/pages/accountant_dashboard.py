import streamlit as st
from supabase import create_client
import datetime

# -- Supabase Setup --
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-or-service-role-key"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="License Accountant Dashboard", layout="wide")
st.title("💰 License Accountant Dashboard")

# -- Get unpaid violations --
def fetch_unpaid_violations():
    response = supabase.table("violations").select("*").eq("paid", False).execute()
    return response.data if response else []

# -- Mark a fine as paid --
def mark_as_paid(violation_id):
    supabase.table("violations").update({
        "paid": True,
        "paid_on": datetime.date.today().isoformat()
    }).eq("id", violation_id).execute()

# -- Show fine history --
def fetch_payment_history(plate_number):
    response = supabase.table("violations").select("*").eq("plate", plate_number).execute()
    return response.data if response else []

# Example: Retrieve user_role from session state or authentication system
user_role = st.session_state.get("user_role", None)

if user_role != "accountant":
    st.error("You do not have permission to access this page.")