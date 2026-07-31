import streamlit as st
import pandas as pd
import re
import inspect
import rag_llm


from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline
)

from llm_topic_classifier import classify_topic
from rag_retrieve import retrieve_context
from rag_llm import generate_response
from recommendation_engine import generate_recommendations

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Telecom AI Brand Intelligence System",
    layout="wide"
)

st.title("📡 Telecom AI Brand Intelligence System")

# =====================================================
# LOAD DISTILBERT MODEL
# =====================================================

MODEL_PATH = "models/distilbert_model"

@st.cache_resource
def load_sentiment_model():

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH
    )

    model = AutoModelForSequenceClassification.from_pretrained(
        MODEL_PATH
    )

    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer
    )

    return sentiment_pipeline

sentiment_pipeline = load_sentiment_model()

# =====================================================
# TEXT CLEANING
# =====================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(
        r"http\S+",
        "",
        text
    )

    text = re.sub(
        r"@\w+",
        "",
        text
    )

    text = re.sub(
        r"[^a-zA-Z\s]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()

# =====================================================
# SENTIMENT PREDICTION
# =====================================================

def get_sentiment(text):

    result = sentiment_pipeline(text[:512])[0]

    label = str(
        result["label"]
    ).upper()

    if label == "LABEL_0":
        return "Negative"

    elif label == "LABEL_1":
        return "Positive"

    elif label == "NEGATIVE":
        return "Negative"

    elif label == "POSITIVE":
        return "Positive"

    return label

# =====================================================
# CUSTOMER FEEDBACK ANALYSIS
# =====================================================

st.header("📝 Customer Feedback Analysis")

feedback = st.text_area(
    "Enter Customer Feedback",
    height=150
)

if st.button("Analyze Feedback"):

    if feedback.strip() == "":

        st.warning(
            "Please enter customer feedback."
        )

    else:

        cleaned = clean_text(
            feedback
        )

        # -------------------------
        # DistilBERT Sentiment
        # -------------------------

        sentiment = get_sentiment(
            cleaned
        )

        # -------------------------
        # LLM Topic Classification
        # -------------------------

        category = classify_topic(
            feedback
        )

        # -------------------------
        # RAG Retrieval
        # -------------------------
        context = retrieve_context(
        feedback
        )

        context = context[:500]

        st.write(inspect.getsource(rag_llm.generate_response))

        st.write("FUNCTION OBJECT:", generate_response)

        ai_response = generate_response(
        feedback,
        context
        )

        st.write("AI_RESPONSE =", ai_response)
        #context = retrieve_context(
            #feedback
        #)

        #context = context[:500]

        
        #st.write(inspect.getsource(rag_llm.generate_response))

        #ai_response = generate_response(
            #feedback,
            #context
        #)
        

        # -------------------------
        # Results
        # -------------------------

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "📊 Sentiment"
            )

            if sentiment == "Positive":

                st.success(
                    sentiment
                )

            elif sentiment == "Negative":

                st.error(
                    sentiment
                )

            else:

                st.warning(
                    sentiment
                )

        with col2:

            st.subheader(
                "🏷️ Service Category"
            )

            st.info(
                category
            )

        st.subheader(
            "📚 Retrieved Context"
        )

        st.info(
            context[:500]
        )

        st.subheader(
            "🤖 AI Generated Response"
        )

        st.success(
            ai_response
        )

# =====================================================
# ANALYST DASHBOARD
# =====================================================

st.markdown("---")

st.header(
    "📈 Telecom Brand Analyst Dashboard"
)

try:

    df = pd.read_csv(
        "telecom_ai_dataset.csv"
    )

    col1, col2, col3 = st.columns(3)

    total_feedback = len(df)

    positive_count = len(
        df[
            df["Sentiment"] == "Positive"
        ]
    )

    negative_count = len(
        df[
            df["Sentiment"] == "Negative"
        ]
    )

    col1.metric(
        "Total Feedback",
        total_feedback
    )

    col2.metric(
        "Positive Feedback",
        positive_count
    )

    col3.metric(
        "Negative Feedback",
        negative_count
    )

    # -------------------------
    # Sentiment Distribution
    # -------------------------

    st.subheader(
        "📊 Sentiment Distribution"
    )

    st.bar_chart(
        df["Sentiment"].value_counts()
    )

    # -------------------------
    # Category Distribution
    # -------------------------

    if "Service_Category" in df.columns:

        st.subheader(
            "📡 Service Category Distribution"
        )

        st.bar_chart(
            df["Service_Category"].value_counts()
        )

    # -------------------------
    # Recommendations
    # -------------------------

    st.subheader(
        "💡 AI Recommendations"
    )

    recommendations = (
        generate_recommendations(df)
    )

    for rec in recommendations:

        st.success(
            rec
        )

    # -------------------------
    # Dataset Preview
    # -------------------------

    st.subheader(
        "📄 Dataset Preview"
    )

    st.dataframe(
        df.head(20)
    )

except Exception as e:

    st.error(
        f"Could not load dataset: {e}"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "🚀 Telecom AI Brand Intelligence System | DistilBERT + FLAN-T5 + FAISS + Streamlit"
)