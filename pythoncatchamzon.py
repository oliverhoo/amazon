import requests
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1517832557&sr=8-1&keywords=%E6%9E%81%E7%AE%80"
r = requests.get(url)
print (r.status_code)
print(r.encoding)
print(r.request.headers)
kv  =  {'user-agent':'Mozilla/5.0'}
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1517832557&sr=8-1&keywords=%E6%9E%81%E7%AE%80"
r = requests.get(url,headers = kv)
print(r.request.headers)
r.encoding = r.apparent_encoding
print(r.text)