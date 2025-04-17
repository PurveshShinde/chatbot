from transformers import pipeline

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline('sentiment-analysis')

def get_mental_health_analysis(user_input):
    # Get sentiment from the user input
    result = sentiment_analyzer(user_input)
    sentiment = result[0]['label']
    confidence = result[0]['score']

    # Customize responses based on sentiment
    if sentiment == 'POSITIVE':
        return {"status": "positive", "message": "It's great to hear you're feeling good! 😊 Keep it up!"}
    elif sentiment == 'NEGATIVE':
        return {"status": "negative", "message": "It seems like you're having a tough time. Do you want to talk about it? 😔"}
    else:
        return {"status": "neutral", "message": "Tell me more, I’m here to listen."}
