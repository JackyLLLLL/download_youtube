import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

import os
os.chdir(r'D:\User\Desktop')  # 使用 Colab 要換路徑使用

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=lZnNBuYU1B0')
print('download...')
print(yt.title)

##print(yt.title)           # 影片標題
##print(yt.length)          # 影片長度 ( 秒 )
##print(yt.author)          # 影片作者
##print(yt.channel_url)     # 影片作者頻道網址
##print(yt.thumbnail_url)   # 影片縮圖網址
##print(yt.views)           # 影片觀看數

yt.streams.filter().get_audio_only().download(filename=f'{yt.title}.mp3')
# 儲存為 mp3
print('ok!')


#https://steam.oxxostudio.tw/category/python/example/youtube-download.html#a3
