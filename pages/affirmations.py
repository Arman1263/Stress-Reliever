import streamlit as st
import random
from datetime import datetime
from utils.gemini_api import generate_daily_affirmation

def show_affirmations():
    """
    Display daily affirmations and motivational quotes
    """
    st.title("✨ Daily Affirmations")
    
    # Introduction
    st.markdown("""
    <div style="background-color: #2A2A2A; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <h3 style="margin-top: 0;">The Power of Positive Affirmations</h3>
        <p>Affirmations are positive statements that can help challenge and overcome negative thoughts and beliefs.
        When you repeat them regularly and believe in them, they can help create positive changes in your mindset and reduce stress.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Get today's date for consistency
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Get or generate the daily affirmation
    if 'daily_affirmation' not in st.session_state or 'affirmation_date' not in st.session_state or st.session_state.affirmation_date != today:
        with st.spinner("Generating your daily affirmation..."):
            st.session_state.daily_affirmation = generate_daily_affirmation()
            st.session_state.affirmation_date = today
    
    # Display the daily affirmation in a special box
    st.markdown(f"""
    <div style="background-color: #2A2A2A; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px;">
        <h3 style="margin-bottom: 20px; color: #98FB98;">Your Affirmation for Today</h3>
        <p style="font-size: 1.5rem; font-style: italic; line-height: 1.6; color: #E0E0E0;">"{st.session_state.daily_affirmation}"</p>
        <p style="margin-top: 20px; font-size: 0.8rem; color: #7B68EE;">✨ Generated specially for you today</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Button to get a new affirmation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Generate New Affirmation", type="primary", use_container_width=True):
            with st.spinner("Creating a new affirmation for you..."):
                st.session_state.daily_affirmation = generate_daily_affirmation()
            st.rerun()
    
    # Horizontal divider
    st.markdown("---")
    
    # Affirmation categories
    st.subheader("Affirmation Categories")
    
    # Two-column layout for affirmation categories
    col1, col2 = st.columns(2)
    
    with col1:
        # Self-Compassion affirmations
        with st.expander("Self-Compassion", expanded=True):
            affirmations = [
                "I am worthy of love and respect, exactly as I am.",
                "I treat myself with the same kindness I offer to others.",
                "My imperfections make me unique and human.",
                "I am learning and growing every day, and that's enough.",
                "I forgive myself for my mistakes and learn from them.",
                "I listen to my needs and honor them as valid and important."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Stress Management affirmations
        with st.expander("Stress Management", expanded=False):
            affirmations = [
                "I breathe in calm and exhale tension with each breath.",
                "I have the power to create peace in my mind and body.",
                "This moment of challenge is temporary and I can move through it.",
                "I release what I cannot control and focus on what I can.",
                "I am stronger than my stress and bigger than my worries.",
                "Each breath brings me closer to calm and clarity."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Confidence affirmations
        with st.expander("Confidence", expanded=False):
            affirmations = [
                "I trust my abilities and embrace new challenges.",
                "I speak my truth confidently and with compassion.",
                "I am capable of achieving what I set my mind to.",
                "My voice matters and deserves to be heard.",
                "I am becoming more confident with each passing day.",
                "I believe in myself, even when facing uncertainty."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
    
    with col2:
        # Gratitude affirmations
        with st.expander("Gratitude", expanded=True):
            affirmations = [
                "I am grateful for the abundance that exists in my life.",
                "Each day brings new blessings for me to appreciate.",
                "I notice and appreciate the small joys in everyday moments.",
                "Gratitude transforms my perspective and opens my heart.",
                "I acknowledge all the good that surrounds me.",
                "I am thankful for my resilience through difficult times."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Growth Mindset affirmations
        with st.expander("Growth Mindset", expanded=False):
            affirmations = [
                "I embrace challenges as opportunities to learn and grow.",
                "My potential is limitless when I persist through obstacles.",
                "I can develop new skills through practice and perseverance.",
                "Each setback contains a lesson that makes me stronger.",
                "I am constantly evolving and becoming a better version of myself.",
                "My intelligence and abilities can be developed through dedication."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
        
        # Balance & Boundaries affirmations
        with st.expander("Balance & Boundaries", expanded=False):
            affirmations = [
                "I honor my needs by setting healthy boundaries.",
                "I create balance between work, rest, and play in my life.",
                "Saying no when necessary is an act of self-respect.",
                "I deserve time to rest and recharge without guilt.",
                "I am in control of where my energy goes.",
                "My well-being is a priority worth protecting."
            ]
            
            for affirmation in affirmations:
                st.markdown(f"""
                <div style="background-color: #1A1A1A; padding: 10px 15px; border-radius: 5px; margin-bottom: 10px;">
                    <p style="margin: 0; font-style: italic;">{affirmation}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Horizontal divider
    st.markdown("---")
    
    # Using affirmations effectively section
    st.subheader("Using Affirmations Effectively")
    
    st.markdown("""
    <div style="background-color: #2A2A2A; padding: 20px; border-radius: 10px;">
        <h4 style="color: #7B68EE;">How to Make Affirmations Work for You</h4>
        
        <p><strong>1. Be consistent</strong> - Repeat your affirmations daily, ideally at the same times (morning and evening work well).</p>
        
        <p><strong>2. Make them personal</strong> - Choose or create affirmations that resonate with your specific needs and challenges.</p>
        
        <p><strong>3. Stay present-focused</strong> - Use present tense ("I am" not "I will be") to affirm what is true now.</p>
        
        <p><strong>4. Feel the emotion</strong> - Connect with the feeling behind the words, not just the words themselves.</p>
        
        <p><strong>5. Combine with action</strong> - Use affirmations to support positive behaviors, not replace them.</p>
        
        <p><strong>6. Be patient and persistent</strong> - Changing thought patterns takes time; give the process several weeks.</p>
        
        <p style="font-style: italic; margin-top: 15px;">Remember: The most effective affirmations feel slightly challenging but still believable to you.</p>
    </div>
    """, unsafe_allow_html=True)
