import streamlit as st
import google.generativeai as genai

# Configure Gemini AI
GOOGLE_API_KEY = "AIzaSyBh5jdoQyLanq8c7pT8YMa1rkUOPWWW7bQ"
genai.configure(api_key=GOOGLE_API_KEY)  # Ensure you're using v1

# Generate Itinerary using Gemini AI
def generate_itinerary(destination, days, budget, interests, travelers, pace):
    prompt = f"""
    Generate a {days}-day travel itinerary for {destination}.
    - Budget: {budget}
    - Interests: {interests}
    - Number of Travelers: {travelers}
    - Travel Pace: {pace}

    Provide a detailed daily plan, including:
    - Morning, afternoon, and evening activities
    - Local food recommendations
    - Must-visit attractions
    - Transport suggestions
    - Free-time activities if applicable
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Use latest version
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "❌ Failed to generate itinerary."
    except Exception as e:
        return f"⚠️ API Error: {str(e)}"

# Streamlit UI
st.title("🌍 TravelGenie - AI Itinerary Generator")
st.markdown("#### Plan your perfect trip in seconds using AI!")

# User Inputs
destination = st.text_input("📍 Destination", placeholder="Enter a city or country")
days = st.slider("📅 Number of Days", 1, 14, 5)
budget = st.selectbox("💰 Budget Level", ["Budget", "Mid-range", "Luxury"])
interests = st.text_area("🎯 Interests (e.g., adventure, food, history)", placeholder="Enter your travel interests")
travelers = st.number_input("👥 Number of Travelers", min_value=1, max_value=20, value=2, step=1)
pace = st.radio("⚡ Travel Pace", ["Relaxed", "Balanced", "Fast-paced"], index=1)

# Generate Itinerary Button
if st.button("Generate Itinerary 🚀"):
    if not destination or not interests:
        st.error("❌ Please fill in all fields.")
    else:
        with st.spinner("Generating your itinerary... ✨"):
            itinerary = generate_itinerary(destination, days, budget, interests, travelers, pace)
        st.success("✅ Here’s your travel plan!")
        st.write(itinerary)
