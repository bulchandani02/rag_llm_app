import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth



dotenv.load_dotenv()

# --- Authentication ---
names = ["Jyotsna Bulchandani", "Shivani Sohaney", "Sreejith Sukumara Menon", "Jaffer Sathick"]
usernames = ["Jyotsna", "Shivani", "Sreejith", "Jaffer"]

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, 
    "MMSI Code Ninja", "abcdef", cookie_expiry_days=30) 

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/Password is incorrect. Please try again.")

if authentication_status == None:
    st.warning("Please login to continue.")

if authentication_status == True:
    st.write("authentication successful")
