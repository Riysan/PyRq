import requests
LIMELE_API_URL = "https://riyblog.shop/limele/api/v2/"

def text(url):
    if url == "":
        return "null"
    else:
        res = requests.get(url)
        return str(res.text)

def json(url):
    if url == "":
        return "null"
    else:
        res = requests.get(url)
        return res.json()

def limele(url):
    if url == "":
        return "null"
    else:
        res = requests.get(LIMELE_API_URL + "?url=" + url)
        r = res.json()
        if r["msg"] == "404":
            print("サーバー又は通信エラーです")
            return "err"
        elif r["msg"] == "200":
            return r["url"]
        else:
            print("例外が発生しました")
            return "err"
