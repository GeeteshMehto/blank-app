import streamlit as st



# Set up the page configuration
st.set_page_config(
    page_title="Welcome to Our App",
    page_icon="✨",
    layout="centered",
)

# Display a header
st.title("Welcome to Our Platform")
st.markdown("""
## Your One-Stop Solution for [Insert Service Here]
Discover the power of AI-driven solutions tailored to your needs. 
We offer a range of services to enhance your business processes 
and deliver remarkable results.

---

### Why Choose Us?
- **Custom Solutions:** Tailored to your specific requirements.
- **Scalable:** Flexible to grow with your business.
- **Secure:** Data privacy and security are our top priorities.

Ready to get started? Click the login button below to access your personalized dashboard.
""")

# Add some spacing
st.write("")

# Create a login button
login_url = "https://YOUR-AUTH0-DOMAIN/authorize?client_id=YOUR-CLIENT-ID&redirect_uri=YOUR-REDIRECT-URI"
if st.button("Login"):
    st.write("Redirecting to login...")
    st.write(f"[Login with Auth0]({login_url})")

# Display additional footer or disclaimer if needed
st.markdown("---")
st.markdown("© 2024 Your Company Name. All rights reserved.")
