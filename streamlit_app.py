import streamlit as st

# Assuming you have these URLs set in your Django backend
login_url = "http://127.0.0.1:8000/login"  # Change to your Django login URL
logout_url = "http://127.0.0.1:8000/logout"  # Change to your Django logout URL

# Initialize session state for the user
if 'user_info' not in st.session_state:
    st.session_state['user_info'] = None

def display_page():
    # Check if the user is logged in
    if st.session_state['user_info']:
        # Display welcome message if user is logged in
        st.title(f"Welcome {st.session_state['user_info']['name']}!")
        st.markdown(f"[Logout]({logout_url})")
    else:
        # Display login button if user is not logged in
        st.title("Welcome Guest")
        if st.button("Login"):
            # Redirect to the login URL (Django Auth0 endpoint)
            st.write(f"[Redirecting to login...]({login_url})")

def main():
    st.set_page_config(
        page_title="Auth0 Example",
        page_icon="🔐",
        layout="centered",
    )
    
    # Display the appropriate page based on login state
    display_page()

if __name__ == "__main__":
    main()
