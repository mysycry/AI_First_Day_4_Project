import os
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize session state for dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Function to toggle dark mode
def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Page configuration
st.set_page_config(page_title="FreightMate™ - Your Freight Comparison Specialist", page_icon="🚚", layout="wide")

# Custom CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    body {{
        font-family: 'Inter', sans-serif;
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'#0f172a' if st.session_state.dark_mode else '#f8fafc'};
    }}
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.7)), url('https://images.unsplash.com/photo-1720538531229-46862d8f0381?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .main-header {
        height: 33vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background-image: linear-gradient(rgba(15, 23, 42, 0.7), rgba(15, 23, 42, 0.7)), url('https://images.unsplash.com/photo-1720538531229-46862d8f0381?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-position: center;
        margin-bottom: 2rem;
    }
    .main-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    .stButton>button {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'#3b82f6' if st.session_state.dark_mode else '#e0f2fe'};
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    .stButton>button:hover {{
        background-color: {'#2563eb' if st.session_state.dark_mode else '#bfdbfe'};
        transform: translateY(-2px);
    }}
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {{
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
        background-color: {'rgba(30, 41, 59, 0.8)' if st.session_state.dark_mode else 'rgba(255, 255, 255, 0.8)'};
        border-radius: 8px;
        border: 1px solid {'#475569' if st.session_state.dark_mode else '#cbd5e1'};
        padding: 0.5rem;
    }}
    .card {{
        background-color: {'rgba(15, 23, 42, 0.8)' if st.session_state.dark_mode else 'rgba(248, 250, 252, 0.8)'};
        backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }}
    .card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
    }}
    .mode-toggle {{
        position: fixed;
        top: 1rem;
        right: 1rem;
        z-index: 1000;
        background-color: {'rgba(15, 23, 42, 0.6)' if st.session_state.dark_mode else 'rgba(248, 250, 252, 0.6)'};
        border-radius: 50%;
        padding: 0.5rem;
        backdrop-filter: blur(5px);
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    .mode-toggle:hover {{
        transform: scale(1.1);
    }}
    @media (max-width: 768px) {{
        .card {{
            padding: 1rem;
        }}
        .main-header {
            height: 25vh;
        }
        .main-title {
            font-size: 2.5rem;
        }
    }}
</style>
""", unsafe_allow_html=True)

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("FreightMate_sample_dataset.csv")

df = load_data()

# Title
st.markdown('<div class="main-header"><h1 class="main-title">FreightMate™ - Your Freight Comparison Specialist</h1></div>', unsafe_allow_html=True)

# Dark mode toggle
st.markdown(
    f"""
    <div class="mode-toggle" onclick="toggleDarkMode()">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            {'<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>' if st.session_state.dark_mode else '<circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>'}
        </svg>
    </div>
    <script>
        function toggleDarkMode() {{
            const streamlitDoc = window.parent.document;
            const darkModeButton = streamlitDoc.querySelector('button[kind="secondary"][aria-label="Toggle dark mode"]');
            if (darkModeButton) {{
                darkModeButton.click();
            }}
        }}
    </script>
    """,
    unsafe_allow_html=True
)


# Content
st.markdown('<div class="card">', unsafe_allow_html=True)
st.write("Welcome to FreightMate™! We help you find the most cost-effective freight options by comparing rates, schedules, and routes.")
st.markdown('</div>', unsafe_allow_html=True)

# Freight Finder
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Find the Best Freight Option")
col1, col2 = st.columns(2)
with col1:
    origin = st.selectbox("Select Origin", df['Origin'].unique())
with col2:
    destination = st.selectbox("Select Destination", df['Destination'].unique())

if st.button("Find Cheapest Freight"):
    filtered_df = df[(df['Origin'] == origin) & (df['Destination'] == destination)]
    if not filtered_df.empty:
        cheapest_freight = filtered_df.loc[filtered_df['Freight Rate (USD)'].idxmin()]
        st.success(f"The cheapest freight option from {origin} to {destination} is:")
        st.json(cheapest_freight.to_dict())
    else:
        st.warning("No direct routes found for the selected origin and destination.")
st.markdown('</div>', unsafe_allow_html=True)

# Rate Calculator
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Freight Rate Calculator")
weight = st.number_input("Enter shipment weight (kg)", min_value=0.1, step=0.1)
distance = st.number_input("Enter shipping distance (km)", min_value=1, step=1)

if st.button("Calculate Estimated Rate"):
    estimated_rate = weight * distance * 0.01  # Example calculation
    st.success(f"Estimated freight rate: ${estimated_rate:.2f}")
st.markdown('</div>', unsafe_allow_html=True)


# RAG Implementation
def get_rag_response(query):
    context = df.to_string()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are FreightMate, a freight comparison specialist. Only answer questions related to freight rates and scheduling."},
            {"role": "user", "content": f"Based on this data: {context}\n\nUser query: {query}"}
        ]
    )
    return response.choices[0].message['content']

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Ask FreightMate™")
user_query = st.text_area("Ask about freight rates and scheduling:", height=100)
if st.button("Submit Question"):
    if user_query:
        with st.spinner("FreightMate™ is thinking..."):
            rag_response = get_rag_response(user_query)
        st.write("FreightMate's Response:")
        st.write(rag_response)
    else:
        st.warning("Please enter a question before submitting.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("© 2024 FreightMate™ | All Rights Reserved")