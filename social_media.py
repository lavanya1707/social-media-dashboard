import streamlit as st

# Replace these with sample data or connect to real APIs
sample_posts = [
    {"platform": "Twitter", "text": "This is a sample tweet!", "username": "SampleUser"},
    {"platform": "Facebook", "text": "This is a sample Facebook post!", "username": "SampleProfile"},
]

st.title("Social Media Dashboard")
st.write("Current posts:")

for post in sample_posts:
    st.write(f"{post['platform']} - {post['username']}")
    st.write(f"{post['text']}")
    st.write("---")

st.info("This is a basic example. For real-time updates and advanced features, consider connecting to social media APIs securely.")
