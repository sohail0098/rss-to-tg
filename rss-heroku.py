import feedparser, os
from time import sleep, ctime
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pymongo import MongoClient

URLS = [url for url in os.environ.get('URLS').split(',')]
API_KEY = os.environ.get('API_KEY') #get your account API_ID/API_KEY from https://my.telegram.org
API_HASH = os.environ.get('API_HASH') #get your account API_HASH from https://my.telegram.org
STRING_SESSION = os.environ.get('STRING_SESSION') #generate STRING_SESSION using API_KEY and API_ID at https://repl.it/@KeselekPermen/UserButt#main.py
MONGO_URL = os.environ.get('MONGO_URL')

KW = [kw for kw in os.environ.get('KW').split(',')] # Keywords to look for in torrent title to include for download.
BL = [bl for bl in os.environ.get('BL').split(',')] # Blacklist to ignore torrents that contain such words in title.
botUserName = '@' + os.environ.get('botUserName')
chatUserName = os.environ.get('chatUserName')
logUserName = os.environ.get('logUserName')

if chatUserName == None:
    chatUserName = botUserName

def sendmsg(title, link):
    entity=client.get_entity(chatUserName) # destination/bot/chat/user username/ID/link (only username in quotes, everything else without quotes)
    print(f'Sending {title} to Telegram Chat!')
    client.send_message(entity=entity,message=f'/mirror{botUserName} {link}')
    if logUserName != None:
        entity2=client.get_entity(logUserName) # log channel username/id/link
        client.send_message(entity=entity2,message=f"**Title:** `{title}`")


with TelegramClient(StringSession(STRING_SESSION), API_KEY, API_HASH) as client:
    dbclient = MongoClient(MONGO_URL)
    db = dbclient.rsstele
    list = db.rsstele
    incr = 1
    while True:
        try:
            print(f"PING~~~!!! - {ctime()}\n{'*'*37} ~~~ #{incr}")
            for url in URLS:
                rss = feedparser.parse(url)
                print(f"Current Feed: {rss.feed.title}")
                for entry in rss.entries:
                    for links in list.find():
                        if entry.title in links['title']:
                            break
                    else:
                        if 'Nyaa' in rss.feed.title:
                            print(f'Title: {entry.title}')
                            sendmsg(entry.title, entry.link)
                            list.insert_one({'author': 'ubot', 'title': entry.title, 'url': entry.link})
                            sleep(5)
                        elif 'RARBG' in rss.feed.title:
                            if any(word in entry.title for word in KW):
                                if any(word in entry.title for word in BL):
                                    continue
                                else:
                                    if '1080p' in entry.title:
                                        print(f'Title: {entry.title}')
                                        sendmsg(entry.title, entry.link)
                                        list.insert_one({'author': 'ubot', 'title': entry.title, 'url': entry.link})
                                        sleep(5)
            print("Sleeping for 60s")
            incr += 1
            sleep(60)

        except KeyboardInterrupt:
            print("Quitting!!!")
            exit()
