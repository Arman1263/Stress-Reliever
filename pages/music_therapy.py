import streamlit as st
import random

# Define music recommendations based on mood
music_recommendations = {
    "Relaxed": [
        {"title": "Calm Waves", "artist": "Nature Sounds", "url": "https://www.example.com/calm_waves.mp3"},
        {"title": "Mellow Piano", "artist": "Soothing Keys", "url": "https://www.example.com/mellow_piano.mp3"},
    ],
    "Happy": [
        {"title": "Sunny Days", "artist": "Bright Beats", "url": "https://www.example.com/sunny_days.mp3"},
        {"title": "Upbeat Vibes", "artist": "Good Mood", "url": "https://www.example.com/upbeat_vibes.mp3"},
    ],
    "Sad": [
        {"title": "Soft Strings", "artist": "Emotional Melodies", "url": "https://www.example.com/soft_strings.mp3"},
        {"title": "Gentle Guitar", "artist": "Acoustic Soul", "url": "https://www.example.com/gentle_guitar.mp3"},
    ],
    "Stressed": [
        {"title": "Deep Breath", "artist": "Mind Relax", "url": "https://www.example.com/deep_breath.mp3"},
        {"title": "Zen Mode", "artist": "Tranquility", "url": "https://www.example.com/zen_mode.mp3"},
    ]
}

def show_music_therapy():
    st.title("🎵 Music Therapy")
    st.write("Music can help you relax, focus, or lift your mood. Select your mood and get music recommendations!")
    
    mood = st.selectbox("How are you feeling today?", list(music_recommendations.keys()))
    
    if mood:
        st.subheader(f"Recommended Music for {mood}")
        tracks = music_recommendations[mood]
        selected_track = random.choice(tracks)
        
        st.write(f"**{selected_track['title']}** - {selected_track['artist']}")
        st.audio(selected_track['url'], format="audio/mp3")
        
        st.write("🔄 Click below for another recommendation:")
        if st.button("Recommend Another Track"):
            selected_track = random.choice(tracks)
            st.write(f"**{selected_track['title']}** - {selected_track['artist']}")
            st.audio(selected_track['url'], format="audio/mp3")
    
import streamlit as st

# Define a dictionary of mood-based music recommendations
music_recommendations = {
    "Relaxed": [
        {"title": "Calm Ocean Waves", "artist": "Nature Sounds", "url": "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"},
        {"title": "Soft Piano", "artist": "Piano Moods", "url": "https://samplelib.com/lib/preview/mp3/sample-6s.mp3"}
    ],
    "Happy": [
        {"title": "Upbeat Acoustic", "artist": "Sunny Tunes", "url": "https://samplelib.com/lib/preview/mp3/sample-9s.mp3"},
        {"title": "Feel-Good Jazz", "artist": "Smooth Jazz Band", "url": "https://samplelib.com/lib/preview/mp3/sample-12s.mp3"}
    ],
    "Focused": [
        {"title": "Deep Concentration", "artist": "Ambient Works", "url": "https://samplelib.com/lib/preview/mp3/sample-15s.mp3"},
        {"title": "Coding Flow", "artist": "Lo-Fi Beats", "url": "https://samplelib.com/lib/preview/mp3/sample-18s.mp3"}
    ],
    "Sleepy": [
        {"title": "Gentle Rain Sounds", "artist": "Nature Ambience", "url": "https://samplelib.com/lib/preview/mp3/sample-21s.mp3"},
        {"title": "Slow Guitar", "artist": "Dreamy Strings", "url": "https://samplelib.com/lib/preview/mp3/sample-24s.mp3"}
    ]
}

def show_music_therapy():
    st.title("🎵 Music Therapy")
    st.subheader("Select your mood to get music recommendations")
    
    mood = st.selectbox("Choose your mood:", list(music_recommendations.keys()))
    
    if mood:
        st.write(f"Here are some recommended tracks for your {mood.lower()} mood:")
        
        for track in music_recommendations[mood]:
            st.write(f"**{track['title']}** - *{track['artist']}*")
            if 'url' in track and track['url']:
                st.audio(track['url'], format="audio/mp3")
            else:
                st.warning("Audio URL not available")


