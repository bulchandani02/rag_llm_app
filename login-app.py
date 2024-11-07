import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth
import os
import dotenv
import uuid

# check if it's linux so it works on Streamlit Cloud
if os.name == 'posix':
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

from langchain_openai import ChatOpenAI, AzureChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage

from rag_methods import (
    load_doc_to_db, 
    load_url_to_db,
    stream_llm_response,
    stream_llm_rag_response,
)

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
