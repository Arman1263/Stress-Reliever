import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import numpy as np

def create_mood_chart(mood_data):
    """
    Create an interactive mood tracking chart
    
    Args:
        mood_data (list): List of mood entries with date and mood level
        
    Returns:
        plotly figure: Interactive mood chart
    """
    if not mood_data:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="No mood data available yet. Start tracking to see your patterns!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor="#1A1A1A",
            paper_bgcolor="#1A1A1A",
            font=dict(color="#E0E0E0")
        )
        return fig
    
    # Convert to DataFrame for plotting
    df = pd.DataFrame(mood_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Create the line chart with custom styling
    fig = px.line(
        df, x='date', y='mood', 
        markers=True,
        labels={"date": "Date", "mood": "Mood Rating (1-10)"},
        hover_data=["notes"]
    )
    
    # Customize the appearance
    fig.update_traces(
        line_color="#7B68EE",
        marker=dict(size=8, color="#7B68EE"),
        hovertemplate="<b>Date:</b> %{x|%B %d, %Y}<br><b>Mood:</b> %{y}/10<br><b>Notes:</b> %{customdata[0]}"
    )
    
    fig.update_layout(
        title={
            'text': 'Your Mood Journey',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'color': '#E0E0E0', 'size': 20}
        },
        xaxis_title="Date",
        yaxis_title="Mood Rating",
        yaxis_range=[0, 10],
        plot_bgcolor="#1A1A1A",
        paper_bgcolor="#1A1A1A",
        font=dict(color="#E0E0E0"),
        hovermode="x unified",
        xaxis=dict(
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0")
        ),
        yaxis=dict(
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0"),
            tickmode='linear',
            tick0=0,
            dtick=1
        )
    )
    
    # Add reference lines for mood levels
    fig.add_shape(
        type="line", line_color="#98FB98", line_width=1, line_dash="dash",
        y0=7, y1=7, x0=0, x1=1, xref="paper"
    )
    fig.add_annotation(
        x=df['date'].iloc[-1] if len(df) > 0 else datetime.now(),
        y=7.2,
        text="Good mood zone",
        showarrow=False,
        font=dict(color="#98FB98", size=10)
    )
    
    return fig

def create_stress_chart(stress_data):
    """
    Create an interactive stress monitoring chart
    
    Args:
        stress_data (list): List of stress entries with date and level
        
    Returns:
        plotly figure: Interactive stress chart
    """
    if not stress_data:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="No stress data available yet. Start monitoring to see your patterns!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor="#1A1A1A",
            paper_bgcolor="#1A1A1A",
            font=dict(color="#E0E0E0")
        )
        return fig
    
    # Convert to DataFrame for plotting
    df = pd.DataFrame(stress_data)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Create the line chart with custom styling
    fig = px.line(
        df, x='date', y='level', 
        markers=True,
        labels={"date": "Date", "level": "Stress Level (1-10)"},
        hover_data=["activities"]
    )
    
    # Customize the appearance
    fig.update_traces(
        line_color="#FF8C00",
        marker=dict(size=8, color="#FF8C00"),
        hovertemplate="<b>Date:</b> %{x|%B %d, %Y}<br><b>Stress:</b> %{y}/10<br><b>Activities:</b> %{customdata[0]}"
    )
    
    fig.update_layout(
        title={
            'text': 'Your Stress Patterns',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'color': '#E0E0E0', 'size': 20}
        },
        xaxis_title="Date",
        yaxis_title="Stress Level",
        yaxis_range=[0, 10],
        plot_bgcolor="#1A1A1A",
        paper_bgcolor="#1A1A1A",
        font=dict(color="#E0E0E0"),
        hovermode="x unified",
        xaxis=dict(
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0")
        ),
        yaxis=dict(
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0"),
            tickmode='linear',
            tick0=0,
            dtick=1
        )
    )
    
    # Add reference lines for stress levels
    fig.add_shape(
        type="line", line_color="#98FB98", line_width=1, line_dash="dash",
        y0=3, y1=3, x0=0, x1=1, xref="paper"
    )
    fig.add_annotation(
        x=df['date'].iloc[-1] if len(df) > 0 else datetime.now(),
        y=2.8,
        text="Low stress zone",
        showarrow=False,
        font=dict(color="#98FB98", size=10)
    )
    
    # Add high stress reference line
    fig.add_shape(
        type="line", line_color="#FF6347", line_width=1, line_dash="dash",
        y0=7, y1=7, x0=0, x1=1, xref="paper"
    )
    fig.add_annotation(
        x=df['date'].iloc[-1] if len(df) > 0 else datetime.now(),
        y=7.2,
        text="High stress zone",
        showarrow=False,
        font=dict(color="#FF6347", size=10)
    )
    
    return fig

def create_activities_impact_chart(stress_data):
    """
    Create a chart showing the impact of different activities on stress levels
    
    Args:
        stress_data (list): List of stress entries with activities and levels
        
    Returns:
        plotly figure: Bar chart of activities and their impact
    """
    if not stress_data or len(stress_data) < 3:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="Not enough data to analyze activities impact yet. Keep tracking!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor="#1A1A1A",
            paper_bgcolor="#1A1A1A",
            font=dict(color="#E0E0E0")
        )
        return fig
    
    # Process the activities data
    activity_stress = {}
    
    for entry in stress_data:
        activities = [a.strip() for a in entry['activities'].split(',')]
        for activity in activities:
            if activity:
                if activity not in activity_stress:
                    activity_stress[activity] = []
                activity_stress[activity].append(entry['level'])
    
    # Calculate average stress for each activity
    activity_avg = {}
    for activity, levels in activity_stress.items():
        if len(levels) >= 2:  # Only include activities with at least 2 data points
            activity_avg[activity] = sum(levels) / len(levels)
    
    # Create DataFrame for visualization
    if not activity_avg:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="Not enough consistent activities to analyze impact yet. Keep tracking!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor="#1A1A1A",
            paper_bgcolor="#1A1A1A",
            font=dict(color="#E0E0E0")
        )
        return fig
    
    df = pd.DataFrame(list(activity_avg.items()), columns=['Activity', 'Average Stress'])
    df = df.sort_values('Average Stress')
    
    # Create horizontal bar chart
    fig = px.bar(
        df, 
        y='Activity', 
        x='Average Stress',
        orientation='h',
        color='Average Stress',
        color_continuous_scale=['#98FB98', '#FFFF00', '#FF8C00'],
        labels={"Activity": "", "Average Stress": "Average Stress Level"}
    )
    
    fig.update_layout(
        title="Activities & Their Impact on Your Stress Levels",
        plot_bgcolor="#1A1A1A",
        paper_bgcolor="#1A1A1A",
        font=dict(color="#E0E0E0"),
        xaxis=dict(
            title="Average Stress Level",
            range=[0, 10],
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0")
        ),
        yaxis=dict(
            gridcolor="#333333",
            tickfont=dict(color="#E0E0E0")
        ),
        coloraxis_showscale=False
    )
    
    return fig

def create_weekly_summary(mood_data=None, stress_data=None):
    """
    Create a weekly summary visualization comparing mood and stress
    
    Args:
        mood_data (list): List of mood entries
        stress_data (list): List of stress entries
        
    Returns:
        plotly figure: Weekly summary chart
    """
    # If both data lists are empty, return message
    if (not mood_data or len(mood_data) < 3) and (not stress_data or len(stress_data) < 3):
        fig = go.Figure()
        fig.add_annotation(
            text="Not enough data for weekly summary. Continue tracking mood and stress!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        fig.update_layout(
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            plot_bgcolor="#1A1A1A",
            paper_bgcolor="#1A1A1A",
            font=dict(color="#E0E0E0")
        )
        return fig
    
    # Get last 7 days dates
    end_date = datetime.now()
    start_date = end_date - timedelta(days=6)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    date_strings = [date.strftime('%Y-%m-%d') for date in date_range]
    
    # Initialize empty data
    weekly_data = {
        'date': date_strings,
        'mood_avg': [None] * 7,
        'stress_avg': [None] * 7
    }
    
    # Process mood data if available
    if mood_data and len(mood_data) > 0:
        mood_df = pd.DataFrame(mood_data)
        mood_df['date'] = pd.to_datetime(mood_df['date']).dt.strftime('%Y-%m-%d')
        
        # Filter for last 7 days and calculate daily averages
        for i, date in enumerate(date_strings):
            day_data = mood_df[mood_df['date'] == date]
            if not day_data.empty:
                weekly_data['mood_avg'][i] = day_data['mood'].mean()
    
    # Process stress data if available
    if stress_data and len(stress_data) > 0:
        stress_df = pd.DataFrame(stress_data)
        stress_df['date'] = pd.to_datetime(stress_df['date']).dt.strftime('%Y-%m-%d')
        
        # Filter for last 7 days and calculate daily averages
        for i, date in enumerate(date_strings):
            day_data = stress_df[stress_df['date'] == date]
            if not day_data.empty:
                weekly_data['stress_avg'][i] = day_data['level'].mean()
    
    # Create a DataFrame from the processed data
    weekly_df = pd.DataFrame(weekly_data)
    weekly_df['display_date'] = pd.to_datetime(weekly_df['date']).dt.strftime('%a, %b %d')
    
    # Create the figure
    fig = go.Figure()
    
    # Add mood line if data exists
    if mood_data and len(mood_data) > 0:
        fig.add_trace(go.Scatter(
            x=weekly_df['display_date'],
            y=weekly_df['mood_avg'],
            mode='lines+markers',
            name='Mood',
            line=dict(color='#7B68EE', width=3),
            marker=dict(size=8, color='#7B68EE')
        ))
    
    # Add stress line if data exists
    if stress_data and len(stress_data) > 0:
        fig.add_trace(go.Scatter(
            x=weekly_df['display_date'],
            y=weekly_df['stress_avg'],
            mode='lines+markers',
            name='Stress',
            line=dict(color='#FF8C00', width=3),
            marker=dict(size=8, color='#FF8C00')
        ))
    
    # Update layout
    fig.update_layout(
    title="Your Week at a Glance",
    xaxis_title="Date",
    yaxis_title="Rating (1-10)",
    yaxis=dict(
        range=[0, 10],
        gridcolor="#333333",
        tickfont=dict(color="#E0E0E0")
    ),
    plot_bgcolor="#1A1A1A",
    paper_bgcolor="#1A1A1A",
    font=dict(color="#E0E0E0"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    xaxis=dict(
        gridcolor="#333333",
        tickfont=dict(color="#E0E0E0")
    )
)
    
    return fig
