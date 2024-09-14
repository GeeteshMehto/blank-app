import streamlit as st

# Assuming you have these URLs set in your Django backend
login_url = "http://127.0.0.1:8000/login"  # Change to your Django login URL
logout_url = "http://127.0.0.1:8000/logout"  # Change to your Django logout URL

# Initialize session state for the user
if 'user_info' not in st.session_state:
    st.session_state['user_info'] = None

# Add custom CSS for navbar and page styling
def add_custom_styles():
    st.markdown(
        """
        <style>
        /* Navbar styling */
        .navbar {
            background-color: powderblue;
            padding: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: black;
        }

        /* General page styling */
        .stApp {
            background-color: #d4e6f2;
            color: black;
        }

        /* Anchor tag styling */
        .no-style-link {
            color: #007bff;  /* Set the text color */
            text-decoration: none;  /* Remove underline */
        }

        .no-style-link:hover {
            color: #0056b3;  /* Change color on hover */
            text-decoration: none;  /* Ensure no underline on hover */
        }

        /* Header and subheader styling */
        .main-header {
            color: black;
        }
        
        .sub-header {
            color: blue;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_page():
    # Add custom styles
    add_custom_styles()

    # Navbar
    st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    # Check if the user is logged in
    if st.session_state['user_info']:
        # Display welcome message if the user is logged in
        st.title(f"Welcome {st.session_state['user_info']['name']}!")
        st.markdown(f"[Logout]({logout_url})")
    else:
        # Display information and login button if the user is not logged in
        st.markdown('<h1 class="main-header">Welcome to [Platform Name]</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="sub-header">Bridging the Gap in Healthcare</h2>', unsafe_allow_html=True)
        st.markdown(
            """
            Are you a **hospital** or a **medical expert** looking to provide high-quality healthcare services to patients, no matter their location?  
            
            At **[Platform Name]**, we bridge the gap between patients in remote areas and medical professionals like you through advanced **telemedicine technology**.
            
            **New to [Platform Name]?** Register as a hospital or medical expert to begin delivering remote healthcare.  
            
            **Sign up now** and start making a difference in patients' lives through telemedicine.  
            Your expertise can save lives.
            """
        )
        
        # Anchor tag styled without default styling
        st.markdown(f'<a href="{login_url}" class="no-style-link"><button class="btn btn-success">Login</button></a>', unsafe_allow_html=True)

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
