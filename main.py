#!/usr/bin/env python
from tkinter.scrolledtext import ScrolledText
from urllib.request import urlopen
from lxml import etree
from tkinter import ttk
from tkinter import *
import threading
import random
import os

def downloadVideo():
    try:
        page = int(random.uniform(1, 9999))
        video_url = "http://magicapi.vmovier.com/magicapiv2/video/shareview?id={}".format(page)
        print("视频ID：\n", page)
        html = urlopen(video_url).read().decode("utf-8")
        url_xpath = etree.HTML(html)
        title = url_xpath.xpath("//*[@id='share-tag']/@sharetitle")[0];print("视频： \n", title)
        blurb = url_xpath.xpath("//*[@id='share-tag']/@sharedefaultdes")[1]
        if blurb == "??" or blurb == "":
            print("简介： \n 暂无")
            blurb = str("暂无")
        else:
            print("简介： \n", blurb)
        label = url_xpath.xpath("//*[@class='num']/text()")[0]
        if label == "##":
            print("标签： \n 未分类")
            label = str("未分类")
        else:
            print("标签： \n", label)
        share = url_xpath.xpath("//*[@class='num']/text()")[1]
        print("分享： \n", share)
        url = url_xpath.xpath("//*[@controls='controls']/@src")[0]
        if url == "":
            print("链接： \n", "这可能是一个假视频. T^T\n")
        else:
            print("链接： \n", url)
        text.insert(END,
                    "视频ID：" + str(page) + "\n" +
                    "视频：" + str(title) + "\n" +
                    "简介：" + str(blurb) + "\n" +
                    "标签：" + str(label) + "\n" +
                    "分享人数：" + str(share) + "\n" +
                    "链接：" + str(url) + "\n\n")
        button.state(['disabled'])
        path = os.getcwd() + "/videos/"
        if not os.path.isdir(path):
            os.mkdir(path)
        with open(path + str(title)+".mp4",'wb') as video:
            var1.set("正在下载，请稍后...  下载速度取决于网速")
            try:
                print("正在下载视频...\n")
                videos = urlopen(url).read()
                video.write(videos)
                var1.set("视频下载完成")
                button.state(['!disabled'])
                print("下载完成！")
                print("=" * 50)
            except:
                video.close()
                os.remove(str(title)+".mp4")
                var1.set("这可能是一个假视频. T^T")
                button.state(['!disabled'])
                print("视频未下载!")
                print("=" * 50)
                pass
    except BaseException as e:
        print(e)
        var1.set("请检查网络！")
        text.insert(END,str("暂无内容，请稍后再试。\n错误代码："+str(e)))
def start():
    th = threading.Thread(target=downloadVideo)
    th.start()

root = Tk()
root.title("魔力盒视频下载器")
root.geometry()
text = ScrolledText(root,font=("微软雅黑",8))
text.grid()
var1 = StringVar()
button = ttk.Button(root,text='下载视频',command=start)
button.grid()
label = Label(root,font=("微软雅黑",10),fg='red',textvariable=var1)
label.grid()
var1.set("准备就绪")
root.mainloop()
