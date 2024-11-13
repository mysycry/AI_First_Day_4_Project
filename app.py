import os
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

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

# Custom CSS
st.markdown(f"""
<style>
    body {{
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
    .main-title {{
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        padding: 2rem 0;
        background-color: {'rgba(15, 23, 42, 0.8)' if st.session_state.dark_mode else 'rgba(248, 250, 252, 0.8)'};
        backdrop-filter: blur(10px);
        border-radius: 15px;
        margin-bottom: 2rem;
        color: {'#ffffff' if st.session_state.dark_mode else '#1e293b'};
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
        background-color: {'rgba(15, 23, 42, 0.8)' if st.session_state.dark_mode else 'rgba(248, 250, 252, 0.8)'};
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

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("FreightMate_sample_dataset.csv")

df = load_data()

# Title
st.markdown('<h1 class="main-title">FreightMate™ - Your Freight Comparison Specialist</h1>', unsafe_allow_html=True)

# Dark mode toggle
st.sidebar.button("Toggle Dark/Light Mode", on_click=toggle_dark_mode)

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
    st.write("- **Cost Savings:** Identify the most cost-effective options for your freight needs.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_tab == "Freight Finder":
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

elif st.session_state.active_tab == "Rate Calculator":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Freight Rate Calculator")
    weight = st.number_input("Enter shipment weight (kg)", min_value=0.1, step=0.1)
    distance = st.number_input("Enter shipping distance (km)", min_value=1, step=1)
    
    if st.button("Calculate Estimated Rate"):
        # This is a simplified calculation. In a real-world scenario, you'd use more complex pricing models.
        estimated_rate = weight * distance * 0.01  # Example calculation
        st.success(f"Estimated freight rate: ${estimated_rate:.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.active_tab == "About":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("About FreightMate™")
    st.write("FreightMate™ is your trusted partner in freight logistics. Our advanced algorithms and comprehensive database ensure that you always get the best rates and routes for your shipments.")
    st.write("### Our Mission")
    st.write("To simplify freight logistics and empower businesses with cost-effective shipping solutions.")
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

# Handle tab selection
for tab in tabs:
    if st.button(tab, key=f"tab_{tab}"):
        st.session_state.active_tab = tab
        st.rerun()