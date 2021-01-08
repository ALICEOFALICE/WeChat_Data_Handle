import hashlib
import random
import string
import time


class sign(object):
    def __init__(self):
        print("test")

    def hexdigest(self, text):
        md5 = hashlib.md5()
        md5.update(text.encode())
        return md5.hexdigest()

    def get_ds(self):
        # v2.3.0-web @povsister & @journey-ad
        n = 'h8w582wxwgqvahcdkpvdhbh2w9casgfl'
        i = str(int(time.time()))
        r = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
        c = self.hexdigest('salt=' + n + '&t=' + i + '&r=' + r)
        return '{},{},{}'.format(i, r, c)


print(sign().get_ds())

# 1610108810,bm6kan,438e5a23e4f07c3d34030d189d48a943
# 1610110504,ff2nij,6fd09b4f9e76f087db453ae76bf470ed
