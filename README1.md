＃亚马逊
第一次在github上面上传东西，记录一下，之前git一直下了，学了一些语法，长时间没有用都生疏了。
前一段时间想要将自己写的一些项目传到网上，但是出现了一些错误没有解决，导致长时间没有碰github。
终于抽出了一些时间，在两个小时的努力解决下，终于解决了，并加深了git的使用。
import requests 引入requestku
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1517832557&sr=8-1&keywords=%E6%9E%81%E7%AE%80"
r = requests.get(url)
print (r.status_code)
print(r.encoding) 打印编码方式
print(r.request.headers)
kv  =  {'user-agent':'Mozilla/5.0'}
url = "https://www.amazon.cn/dp/B01M8L5Z3Y/ref=sr_1_1?ie=UTF8&qid=1517832557&sr=8-1&keywords=%E6%9E%81%E7%AE%80"
r = requests.get(url,headers = kv)
print(r.request.headers)输出headers
r.encoding = r.apparent_encoding
print(r.text)

