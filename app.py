import streamlit as st
import os
from pathlib import Path
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from utils.auth import check_authentication
from utils.gemini_api import initialize_gemini_api
import json


# Set page configuration
st.set_page_config(
    page_title="Mindful - Stress Relief Application",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables if they don't exist
if 'user' not in st.session_state:
    st.session_state.user = None
if 'mood_data' not in st.session_state:
    st.session_state.mood_data = []
if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = []
if 'gemini_initialized' not in st.session_state:
    st.session_state.gemini_initialized = False
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Initialize Gemini API
if not st.session_state.gemini_initialized:
    gemini_api_key = os.getenv("GEMINI_API_KEY", "AIzaSyBJwdy8ByoRp7q1ej251jVBGXWRI5LcWrk")
    initialize_gemini_api(gemini_api_key)
    st.session_state.gemini_initialized = True

# Apply custom styling
def local_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Open+Sans:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Montserrat', 'Open Sans', sans-serif;
        }
        
        .card {
            background-color: #2A2A2A;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        }
        
        .highlight {
            color: #7B68EE;
            font-weight: 600;
        }
        
        .accent {
            color: #FF8C00;
        }
        
        .success {
            color: #98FB98;
        }
        
        .btn-custom {
            background-color: #7B68EE;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        .btn-custom:hover {
            background-color: #6A5ACD;
        }
        
        /* Header styling */
        .stApp header {
            background-color: #1A1A1A !important;
        }
        
        /* Main content area */
        .main .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

local_css()

# Navigation function
def navigate_to(page):
    st.session_state.page = page
    st.rerun()

# User authentication
authenticated, username = check_authentication()

if not authenticated:
    # Login page
    st.title("🧠 Mindful")
    st.subheader("Your personal stress relief companion")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Welcome to Mindful</h3>
            <p>A comprehensive stress relief application designed to help you manage and reduce stress through:</p>
            <ul>
                <li>Personalized mood tracking and stress monitoring</li>
                <li>AI-powered journaling and self-reflection</li>
                <li>Calming music therapy and guided relaxation</li>
                <li>Customized wellness recommendations</li>
                <li>Daily affirmations and motivational support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        with st.expander("About Mindful"):
            st.markdown("""
            Mindful is a comprehensive wellness platform that combines modern technology with proven stress-relief techniques. 
            Our AI-powered features adapt to your needs, providing a personalized experience to help you navigate life's challenges.
            
            Start your journey to a calmer, more balanced life today.
            """)
    
    with col2:
        login_container = st.container()
        login_container.markdown('<div class="card">', unsafe_allow_html=True)
        login_container.subheader("Sign In")
        username = login_container.text_input("Username")
        password = login_container.text_input("Password", type="password")
        
        if login_container.button("Login"):
            if username and password:  # In a real app, validate credentials properly
                st.session_state.user = username
                st.rerun()
            else:
                login_container.error("Please enter both username and password")
        
        login_container.markdown("</div>", unsafe_allow_html=True)
        
        # Quick registration for demo
        register_container = st.container()
        register_container.markdown('<div class="card">', unsafe_allow_html=True)
        register_container.subheader("New User?")
        new_username = register_container.text_input("Choose Username")
        new_password = register_container.text_input("Choose Password", type="password")
        
        if register_container.button("Register"):
            if new_username and new_password:
                st.session_state.user = new_username
                st.success("Account created successfully!")
                st.rerun()
            else:
                register_container.error("Please complete all fields")
        
        register_container.markdown("</div>", unsafe_allow_html=True)

else:
    # Sidebar navigation for authenticated users
    with st.sidebar:
        st.title(f"Welcome, {st.session_state.user}")
        
        # User profile section
        st.markdown(f"""
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="width: 80px; height: 80px; border-radius: 50%; background-color: #7B68EE; 
                 color: white; display: inline-flex; align-items: center; justify-content: center; 
                 font-size: 2rem; font-weight: bold;">
                {st.session_state.user[0].upper()}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu
        st.header("Navigation")
        
        if st.button("📊 Dashboard", use_container_width=True):
            navigate_to("dashboard")
        
        if st.button("📝 Journal", use_container_width=True):
            navigate_to("journal")
        
        if st.button("🎵 Music Therapy", use_container_width=True):
            navigate_to("music_therapy")
        
        
        if st.button("✨ Daily Affirmations", use_container_width=True):
            navigate_to("affirmations")
        
        st.markdown("---")
        if st.button("Logout", type="primary"):
            st.session_state.user = None
            st.rerun()
    
    # Main content area based on navigation
    if st.session_state.page == "home" or st.session_state.page == "dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()
    
    elif st.session_state.page == "journal":
        from pages.journal import show_journal
        show_journal()
    
    elif st.session_state.page == "music_therapy":
        from pages.music_therapy import show_music_therapy
        show_music_therapy()
    
    elif st.session_state.page == "affirmations":
        from pages.affirmations import show_affirmations
        show_affirmations()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888888; font-size: 0.8rem;">
    Mindful: Stress Relief Application By Arman © 2025 | 
    <span style="color: #7B68EE;">Powered by Google Gemini AI</span>
</div>
""", unsafe_allow_html=True)
