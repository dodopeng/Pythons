import urllib.request
import urllib.parse
import random
import json


while True:
    content = input("输入你要翻译的内容(输入q!退出):")
    if(content == 'q!'):
        break

    #代理
    #url='http://www.whatismyip.com.tw'
    iplist=['60.251.63.159:8080','118.180.15.152:8102','120.25.171.183:8080','119.6.136.122:80','183.61.71.112:8888','180.103.131.65:808']
    proxys= random.choice(iplist)
    #print (proxys)
    proxy_support = urllib.request.ProxyHandler({'http': proxys})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')]
    urllib.request.install_opener(opener)

    ##爬虫
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    data={}
    data['type']='AUTO'
    data['i']=content
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    data=urllib.parse.urlencode(data).encode('utf-8')


    req = urllib.request.Request(url,data)
    req.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')]
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print(target)
