import re

import requests
from lxml import etree


class bilibili_info:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ \
88.0.4324.50 Safari/537.36 Edg/88.0.705.29"}

    def get_video_info(self, BVID):
        BVID = BVID
        url = "https://www.bilibili.com/video/" + BVID
        print(url)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ \
        88.0.4324.50 Safari/537.36 Edg/88.0.705.29"}
        url = "https://www.bilibili.com/video/" + str(BVID)
        bilibili_video_web = requests.get(url, headers=headers)
        bilibili_video_html = etree.HTML(bilibili_video_web.text)
        bilibili_video_info_title = bilibili_video_html.xpath("//h1/@title")
        bilibili_video_info_player = bilibili_video_html.xpath('//div[@class="video-data"]/span[@class="view"]/text()')
        bilibili_video_info_dm = bilibili_video_html.xpath('//div[@class="video-data"]/span[@class="dm"]/text()')
        bilibili_video_info_creater = bilibili_video_html.xpath('//div[@class="name"]/a[@report-id="name"]/text()')
        bilibili_video_info_like = bilibili_video_html.xpath('//div[@class="ops"]/span[@class="like"]/text()')
        bilibili_video_info_coin = bilibili_video_html.xpath('//div[@class="ops"]/span[@class="coin"]/text()')
        bilibili_video_info_collect = bilibili_video_html.xpath('//div[@class="ops"]/span[@class="collect"]/text()')
        bilibili_video_info_share = bilibili_video_html.xpath('//div[@class="ops"]/span[@class="share"]/text()')


        for title,player,dm,creater,like,coin,collect,share in zip(bilibili_video_info_title,bilibili_video_info_player,bilibili_video_info_dm,bilibili_video_info_creater,bilibili_video_info_like,bilibili_video_info_coin,bilibili_video_info_collect,bilibili_video_info_share):
            bilibili_video_info_player_num= re.sub("\xa0|·","",player)
            bilibili_video_info_dm_num = dm.strip()
            bilibili_video_info_like_num = like.strip()
            bilibili_video_info_coin_num = coin.strip()
            bilibili_video_info_collect_num = collect.strip()
            bilibili_video_info_share_num = share.strip()
            _result="---BILIBILI视频查询----"+\
            "\n视频名称："+ title + \
            "\n播放量："+ bilibili_video_info_player_num + \
            "\n弹幕数：" + bilibili_video_info_dm_num + \
            "\n点赞数" + bilibili_video_info_like_num + \
            "\n投币数" + bilibili_video_info_coin_num +  \
            "\n收藏数" + bilibili_video_info_collect_num + \
            "\n分享数" + bilibili_video_info_share_num  \

            return    (_result)
