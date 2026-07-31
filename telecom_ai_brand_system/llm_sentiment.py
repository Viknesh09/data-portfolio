from transformers import pipeline

sentiment_llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def classify_sentiment(text):

    prompt = f"""
    Classify the telecom feedback.

    Feedback:
    {text}

    Return only:
    Positive
    Neutral
    Negative
    """

    result = sentiment_llm(
        prompt,
        max_new_tokens=10
    )

    return result[0]["generated_text"].strip()
