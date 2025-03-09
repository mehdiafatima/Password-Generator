import streamlit as st
import random
import string
import re


st.markdown(
    """
    <style>
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(-10px);}
            to {opacity: 1; transform: translateY(0);}
        }
        
        @keyframes pulse {
            0% {box-shadow: 0 0 10px #27AE60;}
            50% {box-shadow: 0 0 20px #27AE60;}
            100% {box-shadow: 0 0 10px #27AE60;}
        }
        
        .strength-message {
            animation: fadeIn 0.8s ease-in-out;
            font-size: 18px;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            transition: all 0.3s ease-in-out;
        }
        
        .weak { background-color: #ffcccb; color: #d32f2f; }
        .medium { background-color: #ffeb99; color: #f57c00; }
        .strong { background-color: #c8e6c9; color: #388e3c; }
        
        .pulse-button {
            animation: pulse 1.5s infinite;
            background-color: #27AE60;
            color: white;
            padding: 10px 15px;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        }
        .pulse-button:hover {
            background-color: #1e8449;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    errors = []

    if len(password) >= 8:
        score += 1
    else:
        errors.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        errors.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        errors.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        errors.append("❌ Include at least one special character (!@#$%^&*).")

    return score, errors

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Checker & Generator")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Password Strength", key="check_button"):
    if password:
        score, errors = check_password_strength(password)
        
        if score == 4:
            st.markdown('<div class="strength-message strong">✅ Strong Password!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="strength-message medium">⚠️ Weak Password - Improve it using these tips:</div>', unsafe_allow_html=True)
            for error in errors:
                st.write(error)
            st.session_state.show_generate_button = True
    else:
        st.error("⚠️ Please enter a password to check!")

if st.session_state.get("show_generate_button", False):
    if st.button("🔄 Generate a Strong Password", key="generate_button", help="Click to generate a secure password"):
        strong_password = generate_strong_password()
        st.success(f"🔐 Strong Password: `{strong_password}`")
        st.text_input("Copy the password:", value=strong_password, key="copy_box")

st.markdown("<br><hr><p style='text-align: center; font-size: 14px;'>Built with ❤️ by Mehdia Fatima Faizi</p>", unsafe_allow_html=True)