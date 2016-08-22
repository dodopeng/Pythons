import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import socket

#获取所有代理ip
def getProxyIp():
    proxy = []
    iplist = []
    for i in range(1,2):
        url =  'http://www.xicidaili.com/nn/'+str(i)
        req= urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
        res= urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        ips = soup.findAll('tr')

        #print(len(ips))
        #print(ips[2])

        for x in range(2,len(ips)):
            ip = ips[x]
            tds=ip.findAll('td')
            #print(tds)
            ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]
            proxy.append(ip_temp)

        #print(proxy)

        for i in range(0,len(proxy)):
            ip = proxy[i].strip().split("\t")
            #print(ip)
            proxy_host = ip[0]+":"+ip[1]
            #print(proxy_host)
            iplist.append(proxy_host)
            #print(len(iplist))
        #print(iplist)
        return iplist

#验证获得的IP地址是否可用
def validateIp(iplist):
    url = 'http://whatismyip.com.tw'
    f = open('E:\ip.txt','w')
    socket.setdefaulttimeout(3)

    for x in range(0,len(iplist)):
        try:
            proxy_host=iplist[x]
            #print(proxy_host)    
            proxy_support = urllib.request.ProxyHandler({'http': proxy_host})
            opener = urllib.request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')]
            res = urllib.request.urlopen(url)
            html = res.read().decode('utf-8')
            f.write(proxy_host+'\n')   
            print(proxy_host)
        except Exception:
            continue
    f.close()       

if __name__ == '__main__':
 proxy = getProxyIp()
 validateIp(proxy)
    
    
