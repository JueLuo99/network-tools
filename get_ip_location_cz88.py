from urllib.request import urlopen
from urllib.request import Request
import json


def get_location(ip, appcode):
    """
    使用纯真 IP 库获取 IP 地址的地理位置

    可在此处购买：https://market.aliyun.com/products/57002002/cmapi00046276.html

    Args:
        ip (str): IP 地址
        appcode (str): appcode 密钥
    Returns:
        dict: 地理位置信息，包含 [province, city, isp]
    """
    host = 'http://cz88.rtbasia.com'
    path = '/search'
    method = 'GET'
    appcode = appcode
    querys = 'ip=' + ip
    bodys = {}
    url = host + path + '?' + querys

    request = Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urlopen(request)
    content = response.read()

    if (content):
        dict_content = json.loads(content.decode('utf-8'))
        if (dict_content['code'] == 200):
            return dict_content['data']
        else:
            raise Exception(f"获取地理位置失败，错误码：{dict_content['code']}，错误信息：{dict_content['errors']}")
