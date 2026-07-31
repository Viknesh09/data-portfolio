from transformers import pipeline

classifier = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def classify_topic(feedback):

    prompt = f"""
    Identify telecom service category.

    Categories:
    Mobile Network
    Broadband Service
    Billing & Payments
    Customer Support
    Service Activation
    General Complaint

    Feedback:
    {feedback}

    Return only category name.
    """

    result = classifier(
        prompt,
        max_new_tokens=20
    )

    return result[0]["generated_text"].strip()