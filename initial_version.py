#!/usr/bin/env python
from urllib.request import urlopen
from lxml import etree

def getVideo(pages):
    print("=" * 50)
    for page in range(1,pages):
        video_url = "http://magicapi.vmovier.com/magicapiv2/video/shareview?id={}".format(page)
        html = urlopen(video_url).read().decode("utf-8")
        url_xpath = etree.HTML(html)
        #标题
        title = url_xpath.xpath("//*[@id='share-tag']/@sharetitle")[0]
        print("视频： \n",title)
        # 简介
        blurb = url_xpath.xpath("//*[@id='share-tag']/@sharedefaultdes")[1]
        print("简介： \n", blurb)
        # 标签
        label = url_xpath.xpath("//*[@class='num']/text()")[0]
        print("标签： \n", label)
        # 分享
        share = url_xpath.xpath("//*[@class='num']/text()")[1]
        print("分享： \n", share)
        #链接
        url = url_xpath.xpath("//*[@controls='controls']/@src")[0]
        print("链接： \n",url)
        print("="*50)
getVideo(int(input("输入：")))
