# Kanye West Twitter Bot

This is an automated Twitter bot that posts daily Kanye's quotes using the [Kanye REST API](https://api.kanye.rest). 
The bot uses 'tweepy' for interacting with Twitter's API and 'schedule' for scheduling the tweets.

## Features
- Fetches a random Kanye West quote from the Kanye REST API.
- Tweets the quote at 06:00 AM (EDT) every day.
- Logs errors in case of failures.

## Installation

### Prerequisites
- Python 3.x installed
- Twitter Developer Account (with API keys and access tokens)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/kanye-tweet-bot.git
   cd kanye-tweet-bot

2. Install dependencies:
    ```sh
    pip install -r requirements.txt

3. Add your Twitter API credentials in the 'create_api()' function inside 'main.py':
    ```sh
    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

## Usage

Run the bot manually:
    ```sh
    python main.py

The bot will keep running and tweet daily at 06:00 AM.

## Limitations

- In this version, I'm using the free Twitter API which does not allow automated posting. You may need an elevated API access level.
- The bot runs indefinitely unless manually stopped.

## Perspectives

- Using a cloud service to run this bot countinously

## Licence

This project is open-source, I made it just for funsies

