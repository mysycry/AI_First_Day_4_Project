import os
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import streamlit.components.v1 as components

# Load environment variables
load_dotenv()

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state for dark mode and active tab
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = True
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Home"

# Function to toggle dark mode
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Page configuration
st.set_page_config(page_title="FreightMate™ - Your Freight Comparison Specialist", page_icon="🚚", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("FreightMate_sample_dataset.csv")

df = load_data()

# Custom CSS for modern 2024 design
st.markdown(f"""
<style>
    body {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'#0f172a' if st.session_state.dark_mode else '#ffffff'};
        font-family: 'Arial', sans-serif;
        transition: background-color 0.3s, color 0.3s;
    }}
    .stApp {{
        background-image: url('https://images.unsplash.com/photo-1720538531229-46862d8f0381?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .main-title {{
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        padding: 2rem 0;
        background-color: {'rgba(15, 23, 42, 0.8)' if st.session_state.dark_mode else 'rgba(255, 255, 255, 0.8)'};
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        border-radius: 15px;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
    }}
    .stButton>button {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'#1e40af' if st.session_state.dark_mode else '#3b82f6'};
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.375rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background-color: {'#1e3a8a' if st.session_state.dark_mode else '#2563eb'};
    }}
    .stTextInput>div>div>input, .stSelectbox>div>div>div {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'rgba(30, 41, 59, 0.8)' if st.session_state.dark_mode else 'rgba(255, 255, 255, 0.8)'};
        border-radius: 0.375rem;
        border: 1px solid {'#475569' if st.session_state.dark_mode else '#cbd5e1'};
    }}
    .stTextArea>div>div>textarea {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'rgba(30, 41, 59, 0.8)' if st.session_state.dark_mode else 'rgba(255, 255, 255, 0.8)'};
        border-radius: 0.375rem;
        border: 1px solid {'#475569' if st.session_state.dark_mode else '#cbd5e1'};
        min-height: 100px;
    }}
    .card {{
        background-color: {'rgba(15, 23, 42, 0.8)' if st.session_state.dark_mode else 'rgba(255, 255, 255, 0.8)'};
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }}
    .tabs {{
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }}
    .tab {{
        padding: 0.5rem 1rem;
        margin: 0 0.5rem;
        border-radius: 0.375rem;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .tab.active {{
        background-color: {'#1e40af' if st.session_state.dark_mode else '#3b82f6'};
        color: #ffffff;
    }}
    .tab:hover {{
        background-color: {'#1e3a8a' if st.session_state.dark_mode else '#2563eb'};
        color: #ffffff;
    }}
    .mode-toggle {{
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 1000;
        background-color: {'#ffffff' if st.session_state.dark_mode else '#333333'};
        border-radius: 50%;
        padding: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition: background-color 0.3s;
    }}
    .mode-toggle:hover {{
        background-color: {'#f1f1f1' if st.session_state.dark_mode else '#444444'};
    }}
    .mode-toggle i {{
        font-size: 1.5rem;
        color: {'#1e293b' if st.session_state.dark_mode else '#f8fafc'};
    }}
    @media (max-width: 768px) {{
        .card {{
            padding: 1rem;
        }}
        .main-title {{
            font-size: 2rem;
            padding: 1rem 0;
        }}
        .tabs {{
            flex-wrap: wrap;
        }}
        .tab {{
            margin: 0.25rem;
        }}
    }}
</style>
""", unsafe_allow_html=True)

# Dark mode toggle button (sun/moon icon)
st.markdown(f"""
    <div class="mode-toggle" onclick="window.parent.postMessage({{"type": "toggle_dark_mode"}}, '*')">
        <i class="fa {'fa-sun' if not st.session_state.dark_mode else 'fa-moon'}"></i>
    </div>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">FreightMate™ - Your Freight Comparison Specialist</h1>', unsafe_allow_html=True)

# Navigation tabs
tabs = ["Home", "Freight Finder", "Rate Calculator", "About"]
st.markdown(
    f"""
    <div class="tabs">
        {''.join(f'<div class="tab{"" if st.session_state.active_tab != tab else " active"}" onclick="handleTabClick(\'{tab}\')">{tab}</div>' for tab in tabs)}
    </div>
    <script>
        function handleTabClick(tab) {{
            const streamlitDoc = window.parent.document;
            const tabButton = streamlitDoc.querySelector(`button[kind="secondary"][aria-label="${{tab}}"]`);
            if (tabButton) {{
                tabButton.click();
            }}
        }}
    </script>
    """,
    unsafe_allow_html=True
)

# Content based on selected tab
if st.session_state.active_tab == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("Welcome to FreightMate™! We help you find the most cost-effective freight options by comparing rates, schedules, and routes.")
    st.write("## What FreightMate™ Does")
    st.write("Our tool analyzes a comprehensive dataset of freight providers to offer you the best shipping solutions tailored to your needs.")
    st.write("## Key Features")
    st.write("- **Efficient Comparison:** Compare freight rates, transit times, and schedules across multiple carriers.")
    st.write("- **Route Optimization:** Find the most efficient routes for your shipments.")
    st.write("- **Cost-Effective Shipping:** Get the best prices for your freight needs.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Freight Finder":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## Find the Best Freight Option")
    origin = st.selectbox("Select your origin city:", df["origin"].unique())
    destination = st.selectbox("Select your destination city:", df["destination"].unique())
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Rate Calculator":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## Rate Calculator")
    weight = st.slider("Select the weight of your freight (in kg):", min_value=0, max_value=500, step=1)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_tab == "About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("## About FreightMate™")
    st.write("FreightMate™ is a cutting-edge freight comparison tool designed to save you time and money. Our tool leverages a large dataset of freight providers to find the most efficient and cost-effective shipping options.")
    st.markdown('</div>', unsafe_allow_html=True)
