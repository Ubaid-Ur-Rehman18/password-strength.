import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    # Check lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    # Check digits
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one digit.")
    
    # Check special characters
    if re.search(r"[@$!%*?&]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character (@$!%*?&).")
    
    return strength, feedback

def main():
    st.title("🔐 Password Strength Meter")
    st.write("Enter a password to check its strength.")
    
    password = st.text_input("Enter your password", type="password")
    expiration = st.number_input("Set password expiration (days):", min_value=1, max_value=365, value=30)
    
    if password:
        strength, feedback = check_password_strength(password)
        
        st.write("### Password Strength:")
        if strength == 5:
            st.success("Strong Password! ✅")
        elif strength >= 3:
            st.warning("Moderate Password. Consider improving it.")
        else:
            st.error("Weak Password! ❌ Consider making it stronger.")
        
        if feedback:
            st.write("### Suggestions:")
            for suggestion in feedback:
                st.write(f"- {suggestion}")
    
    # Footer Section
    st.markdown("""
    <div style='position: fixed; bottom: 0; left: 0; width: 100%; background-color: lightgray; padding: 10px; text-align: center;'>
        <p>Created by Ubaid-ur-Rehman | All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
