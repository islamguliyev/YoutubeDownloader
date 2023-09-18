# 65.YOUTUBE VİDEO YÜKLƏYİCİ

import pytube

url = input("enter video url: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)




