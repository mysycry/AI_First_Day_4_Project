import os
import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Page configuration
st.set_page_config(page_title="FreightMate™ - Your Freight Comparison Specialist", page_icon="🚚", layout="wide")

# Custom CSS
def apply_custom_css():
    st.markdown("""
    <style>
        :root {
            --primary-color: #1E88E5;
            --secondary-color: #FFC107;
            --text-color: #333333;
            --background-color: #F5F5F5;
            --card-bg: #FFFFFF;
            --button-color: #1E88E5;
            --button-text-color: #FFFFFF;
            --button-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        body {
            font-family: 'Roboto', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
        }

        .hero-header {
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://images.pexels.com/photos/19856693/pexels-photo-19856693/free-photo-of-cargo-jet-at-airport.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2');
            background-size: cover;
            background-position: center;
            padding: 4rem 2rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        .main-title {
            color: white;
            font-size: 3.5rem;
            font-weight: 700;
            text-align: center;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }

        .section-divider {
            position: relative;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--primary-color), transparent);
            margin: 3rem 0;
            opacity: 0.7;
        }

        .section-divider::before {
            content: '🚛✈️🚢 🚛✈️🚢 🚛✈️🚢';
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            color: var(--primary-color);
            background: var(--background-color);
            padding: 0 1rem;
        }

        .stButton > button {
            background-color: var(--button-color);
            color: var(--button-text-color);
            border: none;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            font-weight: 600;
            box-shadow: var(--button-shadow);
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            opacity: 0.9;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .stTextInput > div > div > input {
            border-radius: 5px;
        }

        .stSelectbox > div > div > select {
            border-radius: 5px;
        }

        .content-section {
            padding: 2rem 0;
        }

.freight-card {
    background: linear-gradient(135deg, #000000, #8B0000); /* Gradient from black to dark red */
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
    color: #F5F5F5; /* Off-white text color for all content */
}

.freight-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
}

.freight-card h3 {
    margin-bottom: 0.5rem;
    color: #FFFFFF; /* Pure white for headers to stand out */
}

.freight-card p {
    margin: 0.25rem 0;
    color: #F5F5F5; /* Off-white for paragraph text */
    opacity: 0.9; /* Slightly transparent for better readability */
}
    </style>
    """, unsafe_allow_html=True)

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv("FreightMate_sample_dataset.csv")

df = load_data()

# Hero Header with FreightMate™ name
st.markdown('<div class="hero-header"><h1 class="main-title">FreightMate™</h1></div>', unsafe_allow_html=True)

# Apply custom CSS
apply_custom_css()

# Welcome Section
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Welcome to FreightMate™")
st.write("Your Freight Comparison Specialist")
st.write("We help you find the most cost-effective freight options by comparing rates, schedules, and routes.")
st.markdown('</div>', unsafe_allow_html=True)

# Section Divider
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Freight Finder Section
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Find the Best Freight Option")
origin = st.selectbox("Select Origin", df['Origin'].unique())

if origin:
    filtered_df = df[df['Origin'] == origin]
    if not filtered_df.empty:
        st.write(f"Available freight options from {origin}:")
        for _, row in filtered_df.iterrows():
            st.markdown(f"""
            <div class="freight-card">
                <h3>{row['Destination']}</h3>
                <p><strong>Carrier:</strong> {row['Carrier']}</p>
                <p><strong>Freight Rate:</strong> ${row['Freight Rate (USD)']}</p>
                <p><strong>Departure Time:</strong> {row['Departure Time']}</p>
                <p><strong>Transit Time:</strong> {row['Transit Time (Hours)']} hours</p>
                <p><strong>Freight Type:</strong> {row['Freight Type']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning(f"No freight options found from {origin}.")
st.markdown('</div>', unsafe_allow_html=True)

# Section Divider
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Rate Calculator Section
st.markdown('<div class="content-section">', unsafe_allow_html=True)
st.subheader("Freight Rate Calculator")
weight = st.number_input("Enter shipment weight (kg)", min_value=0.1, step=0.1)
distance = st.number_input("Enter shipping distance (km)", min_value=1, step=1)

if st.button("Calculate Estimated Rate"):
    estimated_rate = weight * distance * 0.01  # Example calculation
    st.success(f"Estimated freight rate: ${estimated_rate:.2f}")
st.markdown('</div>', unsafe_allow_html=True)

# Section Divider
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# RAG Implementation Section
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

st.markdown('<div class="content-section">', unsafe_allow_html=True)
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
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.write("© 2024 FreightMate™ | All Rights Reserved")
