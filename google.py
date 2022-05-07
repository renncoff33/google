#!/bin/user/python
# module
try:
    import os,sys,time,requests,bs4
    from bs4 import BeautifulSoup
    from time import sleep
except:
    os.system("pip install requests bs4")
# jelajahi
def jelajahi():
    # banner
    banner = """
\033[1;96m      ____  ___   ___   ____ _     _____
     / ___|/ _ \ / _ \ / ___| |   | ____|
    | |  _| | | | | | | |  _| |   |  _|
    | |_| | |_| | |_| | |_| | |___| |___
     \____|\___/ \___/ \____|_____|_____|
                 \033[1;0m\033[1;41mSEARCHING\033[1;0m
\033[1;96m+\033[1;90m============================================\033[1;96m+
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mAuthor    \033[1;91m: \033[1;93mRenn Syndicate
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mYouTube   \033[1;91m: \033[1;93mRenn sydicate
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mFacebook  \033[1;91m: \033[1;93mRann Syndicatee
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mInstagram \033[1;91m: \033[1;93m@ren7_
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;95mGithub    \033[1;91m: \033[4;92mhttps://github.com/RenSydicate\033[1;0m
\033[1;96m+\033[1;90m============================================\033[1;96m+"""
    os.system("clear")
    print(banner)
    # input
    cari = input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mSearch \033[1;91m> \033[1;92m")
    url = f"https://www.google.com/search?&q={cari}"
    r = requests.get(url)
    mencari = BeautifulSoup(r.text,"html.parser")
    a = mencari.find("div",class_="BNeawe").text
    # output
    print(" [•] Hasil >",a)
jelajahi()
