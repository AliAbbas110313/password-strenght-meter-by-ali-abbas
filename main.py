import streamlit as st
import re

def check_strength(password):
    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[@$!%*?&]", password))
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length < 6:
        return "Weak", "red", 0.2
    elif length < 8 and score < 3:
        return "Moderate", "orange", 0.5
    elif length >= 8 and score >= 3:
        return "Strong", "green", 1.0
    else:
        return "Moderate", "orange", 0.6

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password", type="password")

if password:
    strength, color, progress = check_strength(password)
    st.progress(progress)
    st.markdown(f"**Strength:** <span style='color:{color}; font-size:20px;'>{strength}</span>", unsafe_allow_html=True)
