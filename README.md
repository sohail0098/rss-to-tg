## Disclaimer: This is an extension to the rss-to-tg.py script allowing the scrip to be run on Heroku or Zeet.
#### _To run it on heroku or zeet (or even locally), you need to define the necessary environment variables. They are as follows:_
| KEY | VALUE |
| ------ | ------ |
| URLS | URL1,URL2,URL3 ... List of URLs separated by comma |
| KW | KW1,KW2,KW3... Keywords to check for in torrent titles for rarbg |
| BL | BL1,BL2,BL3... Blacklist to ignore titles containing the words |
| API_KEY | get your account API_ID/API_KEY from https://my.telegram.org |
| API_HASH | get your account API_HASH from https://my.telegram.org |
| STRING_SESSION | generate STRING_SESSION using API_KEY and API_ID at https://repl.it/@KeselekPermen/UserButt#main.py |
| MONGO_URL | MongoDB Atlas URL with password and db name included (select 3.4) |
| botUserName | Bot Username or Group Username without the @ (Example: myMirrotBot) |
| chatUserName (Optional) | Chat/Group username without the @ (Example: MyMirrorGroup). Leave empty to send the msg to bot pm |
| logUserName (Optional) | Log Channel or Log Group Username without @ (Example: myLogChannel) |
## Next comes the deploying part. 
### Top deploy on Heroku, simply clone the repo or download as zip and do the following
```sh
heroku create -a appname
git init
git add .
git commit -m "Commit Message"
heroku git:remote -a appname
git push heroku master
```
### For deploying it on Zeet, just clone the repo, select repo on zeet, set env vars and start rolling. 