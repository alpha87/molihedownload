#!/usr/bin/env python
# @Time    : 2017/3/15
# @Author  : AlPha
# @File    : 魔力盒随机.py
# @Version : 3.5
# @Software: PyCharm Community Edition
# @Blog    : http://alpha87.github.io
from urllib.request import urlopen
from lxml import etree
import random
import os

def getVideo():
    page = int(random.uniform(65,66))
    video_url = "http://magicapi.vmovier.com/magicapiv2/video/shareview?id={}".format(page)
    print("视频ID：\n",page)
    html = urlopen(video_url).read().decode("utf-8")
    url_xpath = etree.HTML(html)
    #标题
    title = url_xpath.xpath("//*[@id='share-tag']/@sharetitle")[0]
    print("视频： \n",title)
    # 简介
    blurb = url_xpath.xpath("//*[@id='share-tag']/@sharedefaultdes")[1]
    if blurb == "??":
        print("简介： \n 暂无")
    else:
        print("简介： \n", blurb)
    # 标签
    label = url_xpath.xpath("//*[@class='num']/text()")[0]
    if label == "##":
        print("标签： \n 未分类")
    else:
        print("标签： \n", label)
    # 分享
    share = url_xpath.xpath("//*[@class='num']/text()")[1]
    print("分享： \n", share)
    #链接
    url = url_xpath.xpath("//*[@controls='controls']/@src")[0]
    if url == "":
        print("链接： \n","这可能是一个假视频. T^T\n")
    else:
        print("链接： \n",url)
    return title,url

def downloadVideo(title,url):
    with open(str(title)+".mp4",'wb') as video:
        try:
            videos = urlopen(url).read()
            video.write(videos)
            print("正在下载视频...\n")
            print("下载完成！")
            print("=" * 50)
        except:
            print("视频未下载!")
            video.close()
            os.remove(str(title)+".mp4")
            print("=" * 50)
            pass

i = 0
while i <3:
    a,b = getVideo()
    downloadVideo(a,b)
    i+=1