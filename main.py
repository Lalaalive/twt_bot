import tweepy
import logging
import requests
import schedule
import time

logger = logging.getLogger()

def create_api():
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

def get_kanyes_quote():
    url = "https://api.kanye.rest"
    response = requests.get(url)

    if response.ok:
        return response.json()["quote"]
    else:
        return "Couldn't fetch Kanye's wisdom today 😔😔😔"
    
def tweet_quote(api):
    quote = get_kanyes_quote()
    try:
        api.update_status(quote)
        logger.info(f"Tweeted: {quote}")
    except Exception as e:
        logger.error("Error posting tweet", exc_info=True)


def run_bot():
    api = create_api()
    tweet_quote(api)

# Schedule the posts daily
schedule.every().day.at("06:00").do(run_bot)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(30)