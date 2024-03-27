from openai import OpenAI

def generate_summary(place_data):
    formatted_reviews = format_reviews(place_data['reviews'])
    text_input = f"""
        Place: {place_data['name']}
        Address: {place_data['formatted_address']}
        Rating: {place_data.get('rating', 'N/A')}
        Reviews: {formatted_reviews}
        Opening Hours: {', '.join(place_data.get('opening_hours', 'N/A'))}

        Please summarize the key points about this place, separating in its positive and negative aspects.
        """
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "The following is a summary of the key points about this place, separated in positive and negative bullet points:"},
            {"role": "user", "content": text_input}
        ]
    )
    return response.choices[0].message.content


def format_reviews(reviews):
    formatted_reviews = []
    for review in reviews:
        rating = review['rating']
        text = review['text']
        formatted_review = f"Rating: {rating}\nReview: {text}\n"
        formatted_reviews.append(formatted_review)
    return "\n".join(formatted_reviews)


