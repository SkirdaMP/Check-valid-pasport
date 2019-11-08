import requests  # импортируем модуль
import re
from bs4 import BeautifulSoup
import hashlib


def passport_validity_check(pasport_serie, pasport_num):
    REQ_STATUS_CODE = 200
    BASE_URL = "http://services.fms.gov.ru/"
    services_url = "http://services.fms.gov.ru/info-service.htm?sid=2000"
    services_result_url = "http://services.fms.gov.ru/info-service-result.htm?sid=2000"
    hash_list = [
        '669cf3532495afd40304eab33106bc94',
        'e9d71c9ff6d2f5de0ba6b50633947d16',
        'c66bb3ca19adff2903fa8731291d6b6b',
        'ea77c2f378cdc327f07b84c311b88782',
        '1e44921e41455c19ef3dbbe442798aba',
        'c948e5bd536655405b3a5abd47f964c3',
        'f50c5a35d604e18c2d47e34383b782b7',
        '51282edec22d43b8e0681f2ddd7d8e78',
        'fbd9f8f9fed8274cd18d59e4697e5359'
    ]
    ReCaptcha = ''
    # pasport_serie = "4612"
    # pasport_num = "962295"

    if __name__ == "__main__":
        with requests.Session() as session:
            ufr = session.get(services_url)
            captcha_head = session.head(BASE_URL + "services/captcha.jpg")
            soup = BeautifulSoup(ufr.text, "html.parser")
            get_uri_mp3 = soup.find(
                "param", {'name': 'FlashVars'}).get("value")
            print(get_uri_mp3)
            pattern = r"services\/captcha-audio\/.{28}\/\d\.mp3\?timestamp=(\d*)"
            # В цикле можно получить все совпадения
            for index_url in range(6):
                match = re.search(pattern, get_uri_mp3.split(",")[index_url])
                url = match.group()
                print(url)
                uri_file_download = "http://services.fms.gov.ru/" + url

                get_file = session.get(uri_file_download)
                # print(get_file.content)
                for count_hash, hash_elem in enumerate(hash_list):
                    if hashlib.md5(get_file.content).hexdigest() == hash_elem:
                        ReCaptcha += str(count_hash + 1)
            data = {'sid': 2000, 'form_name': 'form', 'DOC_NUMBER': pasport_num,
                    'DOC_SERIE': pasport_serie, 'captcha-input': ReCaptcha}
            s = session.post(BASE_URL + "info-service.htm", data=data)
            print(s.status_code)
            answer_about_pasport = session.get(services_result_url)
            soup_1 = BeautifulSoup(answer_about_pasport.text, "html.parser")
            get_answer = soup_1.find("h4", {'class': "ct-h4"}).text
            print(get_answer)
            session.cookies.clear_session_cookies()
    return get_answer

with open("C:/Users/Skirda/Desktop/1_1.txt", "w") as text:
    text.write(passport_validity_check("4612","962295"))
