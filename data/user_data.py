import streamlit as st
import pandas as pd
from datetime import datetime
import json

def initialize_user_data():
    """
    Initialize empty user data structures in session state if they don't exist
    """
    if 'users' not in st.session_state:
        st.session_state.users = {}
    
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

def get_user_profile(username):
    """
    Get a user's profile data, or create it if it doesn't exist
    
    Args:
        username (str): The username
    
    Returns:
        dict: User profile data
    """
    initialize_user_data()
    
    if username not in st.session_state.users:
        st.session_state.users[username] = {
            'profile': {
                'username': username,
                'joined_date': datetime.now().strftime("%Y-%m-%d")
            },
            'mood_data': [],
            'journal_entries': [],
            'stress_data': []
        }
    
    return st.session_state.users[username]

def save_mood_entry(username, entry):
    """
    Save a mood entry for a user
    
    Args:
        username (str): The username
        entry (dict): Mood entry data
    """
    user_data = get_user_profile(username)
    user_data['mood_data'].append(entry)

def save_journal_entry(username, entry):
    """
    Save a journal entry for a user
    
    Args:
        username (str): The username
        entry (dict): Journal entry data
    """
    user_data = get_user_profile(username)
    user_data['journal_entries'].append(entry)

def save_stress_entry(username, entry):
    """
    Save a stress entry for a user
    
    Args:
        username (str): The username
        entry (dict): Stress entry data
    """
    user_data = get_user_profile(username)
    user_data['stress_data'].append(entry)

def get_mood_data(username):
    """
    Get a user's mood data
    
    Args:
        username (str): The username
    
    Returns:
        list: User's mood entries
    """
    user_data = get_user_profile(username)
    return user_data.get('mood_data', [])

def get_journal_entries(username):
    """
    Get a user's journal entries
    
    Args:
        username (str): The username
    
    Returns:
        list: User's journal entries
    """
    user_data = get_user_profile(username)
    return user_data.get('journal_entries', [])

def get_stress_data(username):
    """
    Get a user's stress data
    
    Args:
        username (str): The username
    
    Returns:
        list: User's stress entries
    """
    user_data = get_user_profile(username)
    return user_data.get('stress_data', [])

def export_user_data(username, format='json'):
    """
    Export a user's data in the specified format
    
    Args:
        username (str): The username
        format (str): Export format (json or csv)
    
    Returns:
        str or dict: Exported data in the specified format
    """
    user_data = get_user_profile(username)
    
    if format == 'json':
        return json.dumps(user_data, indent=4)
    
    elif format == 'csv':
        # Convert to DataFrame - this is simplified, real implementation would be more complex
        mood_df = pd.DataFrame(user_data.get('mood_data', []))
        journal_df = pd.DataFrame(user_data.get('journal_entries', []))
        stress_df = pd.DataFrame(user_data.get('stress_data', []))
        
        return {
            'mood_data': mood_df.to_csv(index=False) if not mood_df.empty else "No mood data",
            'journal_entries': journal_df.to_csv(index=False) if not journal_df.empty else "No journal entries",
            'stress_data': stress_df.to_csv(index=False) if not stress_df.empty else "No stress data"
        }
    
    return None
