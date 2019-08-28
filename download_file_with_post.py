import requests  # импортируем модуль

if __name__ == "__main__":
    ufr = requests.post(
        "http://xn--b1afk4ade4e.xn--b1ab2a0a.xn--b1aew.xn--p1ai/services/captcha-audio/804a9f1eb3cbe72367b6f1ee38ed/1.mp3", stream=True)  # делаем запрос
    with open("C:/Users/Skirda/Desktop/1_1.mp3", "wb") as audio:
    	audio.write(ufr.content)
