from video_info import *

print(bilibili_info().get_video_info("BV17f4y1y7uN"))
"""
import requests
from  lxml import  etree
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ \
88.0.4324.50 Safari/537.36 Edg/88.0.705.29"}
BVID="BV17f4y1y7uN"
url = "https://www.bilibili.com/video/" + BVID
bilibili_video_web = requests.get(url, headers=headers)
bilibili_video_html = etree.HTML(bilibili_video_web.text)
bilibili_video_info_player = bilibili_video_html.xpath('//div[@class="video-toolbar report-wrap-module \
report-scroll-module"]/div[@class="ops"]/span[@class="like"]/text()')
print(bilibili_video_info_player)
"""
