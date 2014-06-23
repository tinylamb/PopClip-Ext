# coding:utf-8
__author__ = 'tinylamb'
import urllib
import urllib2
from lxml import html
from os.path import expanduser
import subprocess
import random
import os
#test_url = "https://github.com/harmy/PopClip-Extensions/tree/master/source/BetterTranslate"

def getraw(url , raw_header):
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    #reguler={'re':"http://exslt.org/regular-expressions"}
    rawlist = []
    req = urllib2.Request(url, headers=headers)
    html_source = urllib2.urlopen(req).read()
    parser = html.fromstring(html_source.decode('utf-8','ignore'))
    codefiles = parser.xpath('body//tbody[@data-deferred-content-error]')[0].xpath('./tr')
    for tr in codefiles:
        content = tr.xpath('.//td[@class = "content"]')[0]
        raw = content.xpath('.//a')[0]
        raw_url = ''.join(raw.attrib['href'].split('/blob'))
        rawlist.append(raw_header + raw_url)
    return rawlist

def download(url , project_home):
    file_dir = project_home
    file_name = url.split('/')[-1]
    urllib.urlretrieve(url , file_dir + '/' +file_name)

def main():
    url = os.getenv('POPCLIP_TEXT')
    project = url.split('/')[-1]
    home = expanduser('~') + '/GithubTemp/'
    try:
        os.mkdir(home + project)
    except:
        os.mkdir(home + project + str(round(random.random() , 2)))
    project_home = home + project
    raw_header = "https://raw.githubusercontent.com"
    rawlist = getraw(url ,raw_header)
    for r in rawlist:
        download(r,project_home)
    subprocess.call(["open","-R",home]) # open target dir


if __name__ == '__main__':
    main()



