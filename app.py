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
        /* ... (the rest of the CSS remains the same) ... */
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
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Welcome to FreightMate™")
st.write("Your Freight Comparison Specialist")
st.write("We help you find the most cost-effective freight options by comparing rates, schedules, and routes.")
st.markdown('</div>', unsafe_allow_html=True)

# Freight Finder Section
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

# Rate Calculator Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Freight Rate Calculator")
weight = st.number_input("Enter shipment weight (kg)", min_value=0.1, step=0.1)
distance = st.number_input("Enter shipping distance (km)", min_value=1, step=1)

if st.button("Calculate Estimated Rate"):
    estimated_rate = weight * distance * 0.01  # Example calculation
    st.success(f"Estimated freight rate: ${estimated_rate:.2f}")
st.markdown('</div>', unsafe_allow_html=True)

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
