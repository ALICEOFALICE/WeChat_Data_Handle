import werobot
import re
from MiYouShe import *

robot = werobot.WeRoBot(token='123456789')
test = get_MiYouShe()


@robot.text
def echo(message):
    User = message.content
    MiYouShe = get_MiYouShe()
    if re.match('bh3', User):
        UID = message.content
        UID = re.sub("bh3", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_bh3(UID)
    elif re.match('ys', User):
        UID = message.content
        UID = re.sub("ys", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_ys(UID)
    elif re.match('mys', User):
        UID = message.content
        UID = re.sub("mys", "", UID)
        tag = MiYouShe.get_UID_MiYouShe_info(UID)
    else:
        note = "----------*-----------\n" + "            米哈游查询助手        " + "\n原神查询------ys+米游社UID" \
                                                                            "\n崩坏3查询 ---bh3 + 米游社UID" + "\n米游社查询---mys+米游社UID"
    tag = note
    return tag


robot.run()
