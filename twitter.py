import os
import requests
import tweepy

def authenticate():
    """Authenticate with the Twitter API using credentials from environment variables."""
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_secret = os.getenv("TWITTER_ACCESS_SECRET")
    
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)

def get_quote():
    """Fetch a random philosophical quote from Quotable API."""
    url = "https://api.quotable.io/random?tags=philosophy"
    try:
        response = requests.get(url, verify=False)
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
    """Post a tweet with a philosophical quote."""
    api = authenticate()
    quote = get_quote()
    try:
        api.update_status(quote)
        print("Tweet posted successfully:", quote)
    except Exception as e:
        print("Error posting tweet:", e)

if __name__ == "__main__":
    post_tweet()
