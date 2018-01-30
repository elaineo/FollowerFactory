from TwitterAPI import TwitterAPI
import logging
import json
import time

"""
Fill in your keys before running. https://apps.twitter.com/
"""
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

SCREEN_NAME = 'rogerkver'

def main():
    logging.basicConfig(level=logging.INFO)
    bot = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    cursor = -1
    count = 0

    with open('data.csv', 'a+') as f:
        f.write("close,date \n")
    
    while True:
        if not cursor:
            break
        fans_raw = bot.request('followers/list', {'screen_name': SCREEN_NAME, 'count': 200, 'cursor':cursor, 'skip_status':True, 'include_user_entities': False})
        fans_clean = json.loads(fans_raw.response.text)
        cursor = fans_clean['next_cursor']
        logging.info(cursor)
        fans = [f['created_at'] for f in fans_clean['users']]

        with open('data.csv', 'a') as f:
            for fans in fans_clean['users']:
                f.write("%s,%s \n" % (fans['id'], fans['created_at']) )

        count += 200
        logging.info("count: %s" % count)
        time.sleep(60)

if __name__ == "__main__":
    main()
