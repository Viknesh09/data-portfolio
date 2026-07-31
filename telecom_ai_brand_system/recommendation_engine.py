def generate_recommendations(df):

    recommendations = []

    top_category = (
        df["Service_Category"]
        .value_counts()
        .idxmax()
    )

    recommendations.append(
        f"Most complaints are from {top_category}. Focus improvement efforts here."
    )

    negative_pct = (
        len(df[df["Sentiment"]=="Negative"])
        / len(df)
    ) * 100

    if negative_pct > 40:

        recommendations.append(
            "High negative sentiment detected. Immediate action recommended."
        )

    return recommendations