import requests
import json


class get_MiYouShe:
    def __init__(self):
        self.cookie = ""
        self.headers = {"user_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Geck\
        o) Chrome/81.0.4044.113 Safari/537.36"}

    def get_UID_Follower(self, UID):
        urls = "https://bbs-api.mihoyo.com/user/wapi/getUserFullInfo?gids=2&uid=" + str(UID)
        MIYouShe_json = requests.get(urls, headers=self.headers)
        UID_name = (MIYouShe_json.json())["data"]["user_info"]["nickname"]

        UID_follower = (MIYouShe_json.json())["data"]["user_info"]["achieve"]["followed_cnt"]
        result = ("来了来了，客官您请求粉丝数量信息如下" + "\n用户名：" + UID_name + "\nUID：" + str(UID) + "\n粉丝数：" + str(UID_follower))
        return result
