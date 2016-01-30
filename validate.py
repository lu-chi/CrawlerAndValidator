from bs4 import BeautifulSoup
import requests

def getaddrs(filename):
    result = []
    with open(filename) as fi:
        for line in fi:
            result.append(line[:-1])
    return result
    
def validate(filename):
    if len(filename) == 0:
        return
    addrs = getaddrs(filename)
    url = 'https://www.virustotal.com/vi/ip-address/'
    url += addrs[0]
    url += '/information'
    print url
    headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'accept-encoding':'gzip, deflate, sdch',
               'accept-language':'vi,en;q=0.8',
               'cache-control':'max-age=0',
               'cookie':'__utmt=1; VT_PREFERRED_LANGUAGE=en; __utma=194538546.508165789.1453801379.1454133997.1454134465.7; __utmb=194538546.18.10.1454134465; __utmc=194538546; __utmz=194538546.1454134465.7.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
               'upgrade-insecure-requests':'1',
               'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36}'}
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    fo = open('cymon_validate/' + filename + '.txt', 'w')    
    print soup.find_all('div', {'id':'detected-urls'})
    
    fo.write(addrs[0] + ": " + len(soup.find_all))
    
    fo.close()
    
validate('cymon/blacklist3.txt')