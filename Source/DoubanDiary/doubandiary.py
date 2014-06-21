#encoding:utf-8
import urllib2
from lxml import html
import os
import subprocess
from os.path import expanduser
#test_url = 'http://www.douban.com/people/zhangjiawei/notes'

def fetch(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    reguler={'re':"http://exslt.org/regular-expressions"}
    info = []
    while True:
        req = urllib2.Request(url, headers=headers)
        html_source = urllib2.urlopen(req).read()
        parser = html.fromstring(html_source.decode('utf-8','ignore'))
        diary = parser.xpath('body//div[re:test(@id,"note-\d+")]',namespaces=reguler)
        for d in diary:
            title_info = d.xpath('.//a[@title and re:test(@href,".*\d+")]',namespaces=reguler)[0]
            title = title_info.attrib['title']
            url = title_info.attrib['href']
            date = d.xpath('.//span[@class="pl"]')[0].text
            try:
                comments = d.xpath('.//a[re:test(@href,".*comments")]',namespaces=reguler)[0].text[1:-3]
            except IndexError:
                comments = '0'
            info.append([title,date,comments,url])
        # deal with next page
        for i in range(10):
            try:
                if d.tag=="div" and d.attrib.has_key("class") and d.attrib["class"]=="paginator":
                    break
            except:
                break
            try:
                d = d.getnext()
            except:
                break
        try:
            url = d.xpath('.//link[@rel="next"]')[0].attrib['href']
        except :
            break
    data_str=[]
    for i in info:
        data=''.join([d.encode('utf-8','ignore')+'\t' for d in i])
        data_str.append(data)
    return data_str

def download(url , home):
    url = url.strip()
    info = fetch(url)
    info_txt = open(home + '/info.txt','w')
    for i in info:
        info_txt.write(i + '\n')
    info_txt.close()
    subprocess.call(["open","-R",home]) # open target dir

if __name__ == '__main__':
    #home = os.getenv("HOME")  why return None?
    home = expanduser('~')
    url = os.getenv('POPCLIP_TEXT')
    download(url ,home)
    


