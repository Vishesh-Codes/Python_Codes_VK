#----------------------------------
# Latest Top 10 BBC News Reader
#----------------------------------

import requests
import json

def get_latest_news():
    news = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=fc865a01462e4858b70fe820f5daf602")
    parsed = json.loads(news.content)
    return parsed


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    parsed = get_latest_news()
    # print(parsed('articles'))
    # print(len(parsed('articles')))

    speak("Good evening, you are listening BBC News")

    for i in range(10):
        with open("logNews.txt", "a") as f:
            f.write(f"News - ({i+1}):\n{parsed['articles'][i]['content']}\n\n\n\n\n")

        speak(f"News {i+1}\n{parsed['articles'][i]['content']}")