import werobot
import re
from MiYouShe import *

robot = werobot.WeRoBot(token='123456789')
test = get_MiYouShe()


@robot.text
def echo(message):
    UID = message.content
    test = get_MiYouShe()
    print(UID)
    tag = test.get_UID_MiYouShe_ys(UID)
    return tag


robot.run()
