#查询手机号信息

import requests
from lxml import etree


def get_mobile(phone):
    # 查询手机信息
    url = f"https://ip138.com/mobile.asp?mobile={phone}&action=mobile"

    heads = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=heads)
    # 设置中文显示
    response.encoding = 'utf-8'
    # 解析数据
    e = etree.HTML(response.text)
    data = '\n'.join(e.xpath('//tbody/tr/td/a/text()'))

    # 解析数据
    print(data)

get_mobile(13811711111)