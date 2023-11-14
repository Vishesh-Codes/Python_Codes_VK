#----------------------------------
# Latest Top 10 BBC News Reader
#----------------------------------

import requests
import json

def get_latest_news():
    news = requests.get(f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={your_API_key}")
    parsed = json.loads(news.text)
    return parsed

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == '__main__':
    your_API_key = input("Enter your API from newsapi.org here --> ")
    parsed = get_latest_news()

    speak("Welcome, you are listening BBC News")

    for i in range(10):
        with open("logNews.txt", "a") as f:
            f.write(f"News - ({i+1}):\n\tTopic: {parsed['articles'][i]['title']}\n")
            f.write(f"\tContent: {parsed['articles'][i]['content'][:-14]}\n\n\n\n\n")

        speak(f"News {i+1}\n{parsed['articles'][i]['title']}")
        speak(parsed['articles'][i]['content'][:-14])
    
    speak("BBC News Bulletins ends here. Thanks for listening and have a nice day.")