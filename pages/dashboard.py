import streamlit as st
import pandas as pd
from datetime import datetime
from utils.gemini_api import get_mood_insights
from utils.auth import save_user_data, get_user_data
from utils.visualization import create_mood_chart, create_weekly_summary

def show_dashboard():
    st.title("📊 Your Personal Dashboard")
    username = st.session_state.user
    mood_data = get_user_data(username, 'mood')
    stress_data = get_user_data(username, 'stress')
    
    tab1, tab2, tab3 = st.tabs(["Track Your Mood", "Insights & Recommendations", "Weekly Summary"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.subheader("How are you feeling today?")
            date = st.date_input("Date", datetime.now())
            mood = st.slider("Rate your mood", 1, 10, 5, help="1 = Very low, 10 = Excellent")
            notes = st.text_area("What's on your mind? (optional)", placeholder="Write a few words...")
            
            if st.button("Save Entry", type="primary"):
                entry = {"date": date.strftime("%Y-%m-%d"), "mood": mood, "notes": notes}
                save_user_data(username, 'mood', entry)
                st.success("Your mood has been recorded!")
                st.rerun()
        
        with col2:
            st.markdown(
                """
                <div style="background-color: #2A2A2A; padding: 15px; border-radius: 10px;">
                    <h4>Why Track Your Mood?</h4>
                    <ul style="padding-left: 20px;">
                        <li>Identify patterns and triggers</li>
                        <li>Recognize improvements over time</li>
                        <li>Gain insights into your mental well-being</li>
                        <li>Take control of your emotional health</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )
        
        st.subheader("Your Mood Over Time")
        st.plotly_chart(create_mood_chart(mood_data), use_container_width=True)
    
    with tab2:
        st.subheader("AI-Powered Insights")
        
        if not mood_data or len(mood_data) < 2:
            st.info("Start tracking your mood to receive insights.")
        else:
            with st.spinner("Analyzing your mood patterns..."):
                insights = get_mood_insights(mood_data).replace('\n', '<br>')
                
            st.markdown(
                """
                <div style="background-color: #2A2A2A; padding: 20px; border-radius: 10px;">
                    <h4 style="color: #7B68EE;">Your Personalized Insights</h4>
                    <div style="color: #E0E0E0; line-height: 1.6;">{insights}</div>
                </div>
                """.format(insights=insights),
                unsafe_allow_html=True,
            )
    
    with tab3:
        st.subheader("Your Week at a Glance")
        st.plotly_chart(create_weekly_summary(mood_data, stress_data), use_container_width=True)
        
        if mood_data and len(mood_data) > 0:
            recent_mood = [entry['mood'] for entry in mood_data[-7:] if 'mood' in entry]
            if recent_mood:
                avg_mood = sum(recent_mood) / len(recent_mood)
                st.metric("Average Mood", f"{avg_mood:.1f}/10")
            else:
                st.info("Not enough recent mood data to calculate statistics.")
        else:
            st.info("Start tracking your mood to see weekly statistics and progress.")
