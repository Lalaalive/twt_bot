import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("YOUR_CONSUMER_KEY", 
    "YOUR_CONSUMER_SECRET")
auth.set_access_token("YOUR_ACCESS_TOKEN", 
    "YOUR_ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")