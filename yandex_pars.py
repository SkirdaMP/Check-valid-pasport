import json
import requests
from bs4 import BeautifulSoup
"""Придумать,как запрашивать то,что пользователь хочет узнать. Придумать
как получать полезную информацию со страниц"""


def get_html(url):
    response = requests.get(url)
    return response.text


def put_to_json(dictionary):
    with open("pars_to_json.json", 'w', encoding='utf-8') as jsfile:
        json.dump(dictionary, jsfile, sort_keys=False,
                  indent=4,
                  ensure_ascii=False,
                  separators=(',', ': '))


def parser(html):
    soup = BeautifulSoup(html, "html.parser")
    h2 = soup('h2')
    first_result = dict()
    for inform in h2:
        a_tag_list = inform.find_all('a')
        for a_tag in a_tag_list:
            first_result[a_tag.text] = a_tag.get("href")
    put_to_json(first_result)


def main():
    parser(get_html('https://yandex.ru/search/?text=вселенная&clid=2270455&banerid=6300000000%3A59d2af9949568c001cb6907a&win=301&lr=213'))


if __name__ == "__main__":
    main()
