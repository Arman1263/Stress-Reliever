import streamlit as st
import os
import json
from pathlib import Path

def check_authentication():
    """
    Checks if a user is authenticated in the current session.
    In a production app, this would validate against a database.
    
    Returns:
        tuple: (is_authenticated, username)
    """
    # Check if user exists in session state
    if st.session_state.get('user'):
        return True, st.session_state.user
    
    return False, None

def save_user_data(username, data_type, data):
    """
    Save user-specific data like mood entries or journal entries.
    In a real application, this would connect to a secure database.
    
    Args:
        username (str): The username
        data_type (str): Type of data (mood, journal, etc.)
        data: The data to save
    """
    # In a real app, this would be a database operation
    if data_type == 'mood':
        if 'mood_data' not in st.session_state:
            st.session_state.mood_data = []
        st.session_state.mood_data.append(data)
    
    elif data_type == 'journal':
        if 'journal_entries' not in st.session_state:
            st.session_state.journal_entries = []
        st.session_state.journal_entries.append(data)
    
    # Additional data types can be added here

def get_user_data(username, data_type):
    """
    Retrieve user-specific data.
    
    Args:
        username (str): The username
        data_type (str): Type of data to retrieve
        
    Returns:
        The requested data
    """
    if data_type == 'mood':
        return st.session_state.get('mood_data', [])
    
    elif data_type == 'journal':
        return st.session_state.get('journal_entries', [])
    
    # Default return
    return []

def logout_user():
    """
    Log out the current user by clearing session state
    """
    for key in list(st.session_state.keys()):
        del st.session_state[key]
