import requests
import json

app_id = "3410023e"
app_key = "6f82faaee87b2b823916b58f72f648b6"
word = "hello"
url = f"https://od-api.oxforddictionaries.com/api/v2/entries/en/{word}"
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
r = json.loads(r.text)
print(r["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0])
