# -*- coding: utf-8 -*-

from wit import Wit


def reCaptcha():
    resp = None
    captcha = ''
    client = Wit("BHKRRZVCRA456NELAYDKN5GB72QLVPPB")
    for i in range(1, 7):
        with open("C:/Users/Skirda/Downloads/" + str(i) + ".mp3", "rb") as audio:
            resp = client.speech(audio, None, {'Content-type': 'audio/mpeg3'})
        if str(resp['_text']) == "один":
            captcha += '1'
        if str(resp['_text']) == "два":
            captcha += '2'
        if str(resp['_text']) == "три":
            captcha += '3'
        if str(resp['_text']) == "четыре":
            captcha += '4'
        if str(resp['_text']) == "пять":
            captcha += '5'
        if str(resp['_text']) == "шесть":
            captcha += '6'
        if str(resp['_text']) == "семь":
            captcha += '7'
        if str(resp['_text']) == "восемь":
            captcha += '8'
        if str(resp['_text']) == "девять":
            captcha += '9'
    return captcha
