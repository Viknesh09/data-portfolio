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

st.title("🛠️ Issue Classification System")

def classify_issue(feedback):

    feedback = str(feedback).lower()

    if "rude" in feedback or "behavior" in feedback:

        return "Driver Behavior Issue"

    elif "late" in feedback or "delay" in feedback:

        return "Late Arrival"

    elif "dirty" in feedback or "smell" in feedback:

        return "Vehicle Cleanliness"

    elif "expensive" in feedback or "price" in feedback:

        return "Pricing Complaint"

    elif "cancel" in feedback:

        return "Ride Cancellation"

    elif "app" in feedback or "bug" in feedback:

        return "Application Issue"

    else:

        return "General Feedback"

feedback = st.text_area(
    "Enter Customer Feedback"
)

if st.button("Classify Issue"):

    issue = classify_issue(feedback)

    st.success(
        f"Issue Type: {issue}"
    )
