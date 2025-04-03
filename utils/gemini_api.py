import google.generativeai as genai
import streamlit as st
import os

def initialize_gemini_api(api_key):
    """
    Initialize the Gemini API with the provided API key.
    
    Args:
        api_key (str): The API key for Google Gemini
    """
    genai.configure(api_key=api_key)
    st.session_state.gemini_model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(prompt, max_tokens=1024, temperature=0.7):
    """
    Get a response from the Gemini API based on the given prompt.
    
    Args:
        prompt (str): The prompt to send to the API
        max_tokens (int): Maximum tokens in the response
        temperature (float): Creativity level (0.0-1.0)
        
    Returns:
        str: Generated response
    """
    try:
        if 'gemini_model' not in st.session_state:
            api_key = os.getenv("GEMINI_API_KEY", "AIzaSyC-OdMZx1comjGNWCLnFV-72k1Qi8FLbO4")
            initialize_gemini_api(api_key)
        
        response = st.session_state.gemini_model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=max_tokens,
                temperature=temperature
            )
        )
        
        return response.text
    
    except Exception as e:
        st.error(f"Error connecting to Gemini API: {str(e)}")
        return "I'm having trouble connecting to my AI services right now. Please try again later."

def get_mood_insights(mood_data):
    """
    Generate insights based on user's mood data
    
    Args:
        mood_data (list): List of mood entries
        
    Returns:
        str: AI-generated insights
    """
    if not mood_data or len(mood_data) < 2:
        return "Not enough mood data to generate insights yet. Continue tracking your mood for personalized insights."
    
    # Create prompt with mood data
    mood_text = "\n".join([f"Date: {entry['date']}, Mood: {entry['mood']}/10, Notes: {entry['notes']}" for entry in mood_data[-5:]])
    
    prompt = f"""
    Based on the following recent mood entries from a user, provide helpful insights and gentle suggestions for improving their mental well-being.
    Focus on patterns, potential triggers, and actionable advice. Be compassionate and supportive in your response.
    
    RECENT MOOD ENTRIES:
    {mood_text}
    
    Please provide:
    1. A brief observation of patterns or trends
    2. Potential factors that might be influencing their mood
    3. 2-3 specific, actionable suggestions to help improve their well-being
    4. A supportive, encouraging closing statement
    """
    
    return get_gemini_response(prompt, max_tokens=600, temperature=0.7)

def generate_journal_prompt(mood=None, previous_entries=None):
    """
    Generate a thoughtful journaling prompt based on user's mood and history
    
    Args:
        mood (str, optional): User's current mood
        previous_entries (list, optional): List of previous journal entries
        
    Returns:
        str: AI-generated journal prompt
    """
    context = ""
    
    if mood:
        context += f"The user is currently feeling: {mood}. "
    
    if previous_entries and len(previous_entries) > 0:
        recent_entry = previous_entries[-1]
        context += f"Their most recent journal entry was about: {recent_entry.get('title', 'unknown topic')}. "
    
    prompt = f"""
    {context}
    Create a thoughtful, open-ended journaling prompt to encourage self-reflection and stress relief.
    The prompt should be specific enough to inspire writing but open enough to allow for personal expression.
    It should be supportive, non-judgmental, and focused on mental wellbeing. Make the prompt 1-2 sentences long.
    """
    
    return get_gemini_response(prompt, max_tokens=150, temperature=0.8)

def get_wellness_tips(focus_area):
    """
    Generate wellness tips based on the user's area of focus
    
    Args:
        focus_area (str): Area of health the user wants to focus on
        
    Returns:
        str: AI-generated wellness tips
    """
    prompt = f"""
    Provide practical, evidence-based wellness tips for someone interested in improving their {focus_area}.
    Include:
    1. 3-4 actionable suggestions that can be implemented today
    2. A brief explanation of why each tip is beneficial
    3. One longer-term habit that could be developed over time
    
    Format the response in a friendly, encouraging tone. Focus on small, sustainable changes rather than dramatic lifestyle overhauls.
    """
    
    return get_gemini_response(prompt, max_tokens=500, temperature=0.7)

def generate_daily_affirmation():
    """
    Generate a positive daily affirmation
    
    Returns:
        str: AI-generated affirmation
    """
    prompt = """
    Create an uplifting, positive affirmation that promotes self-compassion, resilience, and mental wellbeing.
    The affirmation should be personal (using "I" statements), present-tense, positive, specific, and brief (1-2 sentences).
    Make it powerful yet believable, avoiding toxic positivity.
    """
    
    return get_gemini_response(prompt, max_tokens=100, temperature=0.8)

def analyze_stress_patterns(stress_data):
    """
    Analyze patterns in stress data and provide recommendations
    
    Args:
        stress_data (list): List of stress level entries
        
    Returns:
        str: AI-generated analysis and recommendations
    """
    if not stress_data or len(stress_data) < 3:
        return "Not enough stress data to analyze patterns. Continue logging your stress levels for personalized insights."
    
    # Format the stress data for the AI
    stress_text = "\n".join([f"Date: {entry['date']}, Stress Level: {entry['level']}/10, Activities: {entry['activities']}" for entry in stress_data[-7:]])
    
    prompt = f"""
    Based on the following stress level entries from a user, analyze patterns and provide helpful recommendations:
    
    {stress_text}
    
    Please provide:
    1. An observation of any patterns in stress levels
    2. Identification of potential stress triggers based on the activities
    3. 2-3 specific stress management techniques that might be beneficial based on this data
    4. A brief recommendation for when/how to implement these techniques
    
    Focus on being practical, supportive, and evidence-based in your analysis.
    """
    
    return get_gemini_response(prompt, max_tokens=500, temperature=0.7)
