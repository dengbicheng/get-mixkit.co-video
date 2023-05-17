from urllib.request import urlretrieve
import urllib
import random
url="""
https://assets.mixkit.co/videos/download/mixkit-people-pouring-a-warm-drink-around-a-campfire-513-4K.mp4
"""# 请求下载文件地址
filename = "C:\\Users\\19456\\Videos\\Captures\\mixkit\\"+"123"+'.mp4'


urlretrieve(url, '1.qcel')  # 第二个参数表示路径

opener = urllib.request.build_opener()
# 构建请求头列表每次随机选择一个
ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62',
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
           'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
           ]
opener.addheaders = [('User-Agent', random.choice(ua_list))]
urllib.request.install_opener(opener)
urlretrieve(url, '1.qcel')
