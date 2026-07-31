# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import streamlit as st

from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot & Multilingual Support")

st.write(
    "Customer and Driver Support System"
)

# -----------------------------
# CHATBOT RESPONSES
# -----------------------------

responses = {

    "refund":
    "Refund will be processed within 3-5 business days.",

    "booking":
    "Your ride booking has been confirmed.",

    "cancel":
    "You can cancel your ride before driver arrival.",

    "driver":
    "Your assigned driver is arriving shortly.",

    "payment":
    "Payment support request has been generated.",

    "eta":
    "Estimated arrival time is available in the app.",

    "price":
    "Dynamic pricing depends on demand and traffic.",

    "earnings":
    "Drive during peak demand hours and maintain a high driver rating to maximize earnings.",

    "navigation":
    "Please verify GPS permissions and ensure your internet connection is active.",

    "gps":
    "Please verify GPS permissions and ensure your internet connection is active.",

    "traffic":
    "Heavy traffic may increase travel time and fare estimates.",

    "rating":
    "Maintaining a high driver rating improves ride assignments.",

    "support":
    "Our support team is available 24/7 to assist you.",

    "hello":
    "Hello! Welcome to RideFlow AI Support.",

    "hi":
    "Hi! How can I help you today?"
}

# -----------------------------
# CHATBOT FUNCTION
# -----------------------------

def chatbot(query):

    query = query.lower()

    # Driver queries
    if (
        "driver" in query
        or "டிரைவர்" in query
        or "ड्राइवर" in query
    ):
        return "Your assigned driver is arriving shortly."

    # Refund queries
    elif (
        "refund" in query
        or "money back" in query
        or "பணம்" in query
        or "ரிபண்ட்" in query
        or "रिफंड" in query
    ):
        return "Refund will be processed within 3-5 business days."

    # Cancellation queries
    elif (
        "cancel" in query
        or "ரத்து" in query
        or "रद्द" in query
    ):
        return "You can cancel your ride before driver arrival."

    # Earnings queries
    elif (
        "earnings" in query
        or "income" in query
        or "வருமானம்" in query
        or "कमाई" in query
    ):
        return "Drive during peak demand hours and maintain a high driver rating to maximize earnings."

    # Navigation queries
    elif (
        "navigation" in query
        or "gps" in query
        or "வழிசெலுத்தல்" in query
        or "नेविगेशन" in query
    ):
        return "Please verify GPS permissions and ensure your internet connection is active."

    # Original keyword matching
    for key in responses:

        if key in query:

            return responses[key]

    return "Please contact RideFlow AI customer support."

# -----------------------------
# USER INPUT
# -----------------------------

query = st.text_input(
    "Ask Your Question"
)

# -----------------------------
# LANGUAGE SELECTION
# -----------------------------

language = st.selectbox(

    "Select Language",

    [

        "English",

        "Tamil",

        "Hindi"
    ]
)

# -----------------------------
# RESPONSE BUTTON
# -----------------------------

if st.button("Get Response"):

    if query.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        response = chatbot(query)

        # -----------------------------
        # TRANSLATION
        # -----------------------------

        if language == "Tamil":

            response = GoogleTranslator(

                source='auto',

                target='ta'

            ).translate(response)

        elif language == "Hindi":

            response = GoogleTranslator(

                source='auto',

                target='hi'

            ).translate(response)

        # -----------------------------
        # DISPLAY RESPONSE
        # -----------------------------

        st.success(response)

# %%
