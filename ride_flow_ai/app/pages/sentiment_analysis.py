import streamlit as st

from transformers import pipeline

st.title("🧠 DistilBERT Sentiment Analyzer")

classifier = pipeline(

    "sentiment-analysis",

     model=r"D:\Guvi\Projects\ride_flow_ai\models\distilbert_sentiment_model",

    tokenizer=r"D:\Guvi\Projects\ride_flow_ai\models\distilbert_sentiment_model"
)

review = st.text_area(
    "Enter Customer Feedback"
)

if st.button("Analyze Sentiment"):

    result = classifier(review)

    label = result[0]['label']

    score = result[0]['score']

    if label == "LABEL_0":

        sentiment = "Negative 😠"

    else:

        sentiment = "Positive 😊"

    st.success(
        f"Sentiment: {sentiment}"
    )

    st.write(
        f"Confidence Score: {score:.2f}"
    )