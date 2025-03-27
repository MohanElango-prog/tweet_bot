import os
import requests
import tweepy

def authenticate():
    """Authenticate using Twitter API v2."""
    client = tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
    )
    return client


def get_quote():
    """Fetch a random philosophical quote from Quotable API."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{data['content']} - {data['author']}"
        else:
            print("Failed to fetch quote, using fallback.")
            return "The only true wisdom is in knowing you know nothing. - Socrates"
    except Exception as e:
        print("Error fetching quote:", e)
        return "The only true wisdom is in knowing you know nothing. - Socrates"

def post_tweet():
    """Post a tweet using Twitter API v2."""
    client = authenticate()
    quote = get_quote()
    try:
        response = client.create_tweet(text=quote)
        print("Tweet posted successfully:", response.data)
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    post_tweet()
