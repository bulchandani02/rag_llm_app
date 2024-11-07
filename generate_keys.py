import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Jyotsna Bulchandani", "Shivani Sohaney", "Sreejith Sukumara Menon", "Jaffer Sathick"]
usernames = ["Jyotsna", "Shivani", "Sreejith", "Jaffer"]
passwords = ["Welcome@123", "Welcome@123", "Welcome@123", "Welcome@123"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)