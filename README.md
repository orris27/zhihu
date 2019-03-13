## 环境

1. Chrome Version:  Version 70.0.3538.77 (Official Build) (64-bit)

2. chromedriver version:  2.44

3. Scrapy (1.5.0)
4. selenium (3.12.0)
5. Python 3.6.4 :: Anaconda, Inc.
6. fake-useragent (0.1.11)
7. 操作系统环境

```
orris@orris-Laptop:~/fun/webcrawler/scrapy/zhihu/zhihu$ uname -r
4.13.0-46-generic
orris@orris-Laptop:~/fun/webcrawler/scrapy/zhihu/zhihu$ uname -m
x86_64
orris@orris-Laptop:~/fun/webcrawler/scrapy/zhihu/zhihu$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 17.10
Release:	17.10
Codename:	artful
```



## 使用方法:



配置chromedriver的位置

```
vim settings.py

# 下面这一行修改到指定的chromedriver位置

DRIVER_PATH = "/home/orris/dataset/2.44/chromedriver"
```



先运行selenium_login.py后扫二维码登录，然后等待30秒钟关闭。注意不要关闭打开的浏览器。获得cookies（cookies默认保存在data/cookies下，可以在settings.py中修改）

```
python selenium_login.py
```



然后开始爬虫

```
scrapy crawl zhihuSpider 
```





采集到的数据可以在data/users下面看到。按照人物分类。



## 完成情况

1. 爬取用户数据： 爬取到的用户数据会存储在data/users下面。里面已经有之前爬取过的数据了。
2. 爬取post数据：根据selenium自动登录，使用cookies（在Request中添加cookies参数即可以爬取POST数据，但是由于知乎POST数据较少，且爬取会封IP，所以代码里默认不使用cookies）
3. 断点续爬：使用文件名用name的形式标注已经记录过，不用再次IO。但是相同的link还是会去访问。此外也可以考虑使用`-s JOBDIR=any_dir`来指定。
4. 反反爬虫：使用随机的USER_ANGENTS来实现（这里使用fake-useragent 库）。还可以切换ip代理池，这里没做，因为代理ip需要花钱
5. 登录：运行selenium_login.py就可以登录了，不过需要人工扫描二维码。这也是我们讨论的结果，因为无法实现自动登录，还是需要人为操作……
