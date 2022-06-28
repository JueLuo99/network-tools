import requests


def icp_vvhan(domain):

    url = "https://api.vvhan.com/api/icp"

    querystring = {"url": domain}

    response = requests.request("GET", url, params=querystring)

    if response.json()["success"] == True:
        return response.json()


def icp_yinhu(domain, apikey):

    url = "https://api.yinhu3.com/api/icp"

    querystring = {"domain": domain, "apiKey": apikey}

    response = requests.request("GET", url, params=querystring)

    return response.json()


if __name__ == '__main__':
    res = icp_yinhu("https://www.baidu.com")
