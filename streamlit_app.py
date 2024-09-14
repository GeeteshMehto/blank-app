import streamlit as st

# Assuming you have these URLs set in your Django backend
login_url = "http://127.0.0.1:8000/login"  # Change to your Django login URL
logout_url = "http://127.0.0.1:8000/logout"  # Change to your Django logout URL

# Initialize session state for the user
if 'user_info' not in st.session_state:
    st.session_state['user_info'] = None

# Add custom CSS to change the background color
def add_background_color():
    # Change the background color here (e.g., #f0f0f0 for a light gray background)
    background_color = "d4e6f2"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {background_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def display_page():
    # Add background color
    add_background_color()
    
    # Check if the user is logged in
    if st.session_state['user_info']:
        # Display welcome message if the user is logged in
        st.title(f"Welcome {st.session_state['user_info']['name']}!")
        st.markdown(f"[Logout]({logout_url})")
    else:
        # Display information and login button if the user is not logged in
        st.title("Welcome to [Platform Name]")
        st.header("Bridging the Gap in Healthcare")
        st.markdown(
            """
            Are you a **hospital** or a **medical expert** looking to provide high-quality healthcare services to patients, no matter their location?  
            
            At **[Platform Name]**, we bridge the gap between patients in remote areas and medical professionals like you through advanced **telemedicine technology**.
            
            **New to [Platform Name]?** Register as a hospital or medical expert to begin delivering remote healthcare.  
            
            **Sign up now** and start making a difference in patients' lives through telemedicine.  
            Your expertise can save lives.
            """
        )
        
        # Inject JavaScript to auto-redirect to login on button click
        if st.button("Login"):
            # JavaScript to auto-redirect
            redirect_script = f"""
            <script type="text/javascript">
                window.location.href = "{login_url}";
            </script>
            """
            st.markdown(redirect_script, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="[Platform Name] Telemedicine",
        page_icon="🏥",
        layout="centered",
    )
    
    # Display the appropriate page based on login state
    display_page()

if __name__ == "__main__":
    main()
