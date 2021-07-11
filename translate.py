import random
import time  # 时间戳
import json  # 返回json 处理
import requests  # 请求 url
import hashlib  # md5 加密


def translate(word):
    # set baidu develop parameter
    apiurl = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    appid = '20201218000650218'
    secretKey = '6QDHOEEGLRqSvc7JeuRk'
    time.sleep(1)
    return translateBaidu(apiurl, appid, secretKey, word, 'en', 'zh')


# 翻译内容 源语言 翻译后的语言
def translateBaidu(apiurl, appid, secretKey, content, fromLang='en', toLang='zh'):
    salt = str(random.randint(32768, 65536))
    sign = appid + content + salt + secretKey  # appid+q+salt+密钥 的MD5值
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()  # 对sign做md5，得到32位小写的sign
    try:
        # 根据技术手册中的接入方式进行设定
        paramas = {
            'appid': appid,
            'q': content,
            'from': fromLang,
            'to': toLang,
            'salt': salt,
            'sign': sign
        }
        response = requests.get(apiurl, paramas)

        jsonResponse = json.loads(response.text)  # 获得返回的结果，结果为json格式
        dst = jsonResponse.get('trans_result')[0]["dst"]
        print('translate success ! ')
        return dst
    except Exception as e:
        print('err:', e)
        print(content)
