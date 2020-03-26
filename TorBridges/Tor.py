#! /usr/bin/env python

import base64
from termcolor import colored
import re
import cv2
from bs4 import BeautifulSoup
import pytesseract 
import numpy as np
from os import system, popen
from sys import argv
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
import requests
from inscriptis import get_text
import threading


# signal Tor for a new connection 
def switchIP():
    """switch new ip tor bypass block ip"""
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password = "")
        controller.signal(Signal.NEWNYM)



# get input for run while
input_while = int(argv[1])


# for save bridegs in file txt
def save_bridges(bridges):
    with open("Tor_Bridge/Savedـbridges/tor_BD.txt", "a") as file:
        file.write(bridges)
        file.close()
    


tor_requests = requests.session() # save session requests

# get key captcha_challenge_field and get text in image captcha
def captcha_challenge_field_and_get_text_img():
    """for post data we need to captcha_challenge_field"""

    global captcha_challenge, send_request, url_target  #  global variable 
    tor_requests.proxies = { # set proxy on session requests
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
    }
    url_target = "https://bridges.torproject.org/bridges?transport=obfs4"
    send_request = tor_requests.get(url_target).text
    soup_bs4 = BeautifulSoup(send_request, "lxml")
    soup_find = soup_bs4.find("input", id="captcha_challenge_field")
    search_tag = re.findall("value=.*.>",str(soup_find))
    data_replace1  = str(search_tag).replace("value=", "")
    data_replace2 = str(data_replace1).replace("]", "")
    data_replace3 = str(data_replace2).replace("[", "")
    data_replace4 = str(data_replace3).replace("/", "")
    data_replace5 = str(data_replace4).replace(">", "")
    data_replace6 = str(data_replace5).replace("'", "")
    data_replace7 = str(data_replace6).replace('"', "")
    data_replace8 = str(data_replace7).replace(')', "")
    data_replace9 = str(data_replace8).replace('(', "")
    captcha_challenge = data_replace9


# get image captcha and save image
def get_img_captcah():
    # get image captcha save on file!
    soup = BeautifulSoup(send_request, "lxml")
    soup_data = soup.find("img")
    base64_data = re.findall('./9.*', str(soup_data))
    soup_data1 = str(base64_data).replace("[", "")
    soup_data2 = str(soup_data1).replace("]", "")
    soup_data3 = str(soup_data2).replace("'", "")
    soup_data4 = str(soup_data3).replace('/>', "")
    soup_data5 = str(soup_data4).replace('"', "")
    soup_data6 = str(soup_data5).replace(',', "")
    f = open("Tor_Bridge/image/img_cpatcha_one.jpeg", "wb")
    f.write(base64.b64decode(soup_data6))
    f.close()



# processing imgae captcha and extract text on image
def processing_img_captcha():
        global text_img
        image_open = cv2.imread("Tor_Bridge/image/img_cpatcha_one.jpeg", cv2.IMREAD_COLOR)
        img_orginal = cv2.GaussianBlur(image_open, (9,9),20)
        text_img = pytesseract.image_to_string(img_orginal, lang='eng')


# send data to web page
def send_post_data_to_web_page():
    thread_3 = threading.Thread(target=captcha_challenge_field_and_get_text_img)
    thread_3.start()
    thread_3.join()
    thread_4 = threading.Thread(target=get_img_captcah)
    thread_4.start()
    thread_4.join()
    thread_5 = threading.Thread(target=processing_img_captcha)
    thread_5.start()
    thread_5.join()

    headers = {
                "Host": "bridges.torproject.org",
                "User-Agent": UserAgent().random,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "437",
                "Origin": "null",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
                }
    query = {'captcha_challenge_field': captcha_challenge, 'captcha_response_field': text_img, 'submit': 'submit'}

    post_data = tor_requests.post(url_target, data=query, headers=headers)
    soup_post = BeautifulSoup(post_data.text, "lxml")
    find_post = soup_post("div", id="bridgelines")
    if str(find_post) == "[]":
        print(colored("[-] not found bridegs try agine!", "red"))
        tor_requests.cookies.clear()
        tor_requests.close()

    else:
        get_str = get_text(str(find_post)).replace('[', '').replace(']', '')
        print(colored("[+] found bridegs!\n", "green"), colored(get_str, "green"))
        save_bridges(get_str) # save bridges on the file txt 
        # tor_requests.cookies.clear_expired_cookies()
        tor_requests.cookies.clear_session_cookies()
        tor_requests.cookies.clear()
        tor_requests.close()
        switchIP()


    

def main():
    run = 0
    while True:
        run += 1
        if run == input_while:
            break;
        send_post_data_to_web_page()

if __name__ == "__main__":
    main()