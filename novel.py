# 小说下载器

# 导入请求包
import requests
from lxml import etree

# 链接
url = "https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/1.html"

while True:
    # 伪装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    # 发送请求
    response = requests.get(url, headers=headers)
    # 设置编码
    response.encoding = 'utf-8'
    # 响应信息
    """
    这行代码将 response.text（通常是一个包含HTML内容的字符串）解析成一个 etree 对象 e。
    etree.HTML 函数会将HTML字符串转换为一个可以使用XPath查询的树结构。
    """
    e = etree.HTML(response.text)

    """
    这行代码使用XPath表达式 //div[@class="m-post"]/p/text() 来查找所有位于 class 为 m-post 的 div 标签内的 p 标签的文本内容。
    e.xpath 返回一个包含所有匹配文本的列表。
    '\n'.join(...) 将这些文本内容用换行符 \n 连接起来，形成一个字符串，并赋值给变量 info。
    """
    info = '\n'.join(e.xpath('//div[@class="m-post"]/p/text()'))

    """
    这行代码使用XPath表达式 //h1/text() 来查找所有 h1 标签的文本内容。
    e.xpath 返回一个包含所有匹配文本的列表。
    [0] 表示取列表中的第一个元素，即第一个 h1 标签的文本内容，并赋值给变量 title。
    """
    title = e.xpath('//h1/text()')[0]
    url = f'https://dldl1.nsbuket.cc/{e.xpath("//tr/td[2]/a/@href")[0]}'

    # 保存
    with open('斗罗大陆.txt', 'w', encoding='utf-8') as f:
        f.write(title + '\n\n' + info + '\n\n')
    '''
    退出循环
    '''
    if url == 'https://dldl1.nsbuket.cc/xiaoshuo/douluodalu/':
        break
