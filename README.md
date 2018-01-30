# FollowerFactory
Create the scatterplots used in [NYTimes' Follower Factory](https://www.nytimes.com/interactive/2018/01/27/technology/social-media-bots.html).

### Getting Started
Install dependencies. 
```
pip install TwitterAPI
```

Edit `ff.py` for your account. Go to https://apps.twitter.com/ to get your API keys. 
Don't forget to fill in your screen name.

```
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

SCREEN_NAME = 'eiaine'
```

Run!
```
python ff.py
```

This can take a long time due to Twitter's rate-limiting, so expect to wait about an hour for every 12,000 followers. When the script is complete, view results by opening `index.html` in your web browser. Your plot will look something like this:

<img src="https://raw.githubusercontent.com/elaineo/FollowerFactory/master/eiaine.png" width="900">
