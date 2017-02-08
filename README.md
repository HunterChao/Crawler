### 本仓库下包括拉钩、豆瓣和链家三个爬虫
### 拉钩抓取全部公司介绍信息
##### 运行文件为lagou.py,由于拉钩网对ip有限制，采用更换代理ip的形式进行反爬虫，0103.txt为可用的代理ip，运行时lagou.py随机使用代理ip
##### 拉钩抓取数据部分截图
![](https://github.com/HunterChao/Crawler/blob/master/lagou/screenshots/lagou_pic.png)
### 链家抓取二手房信息数据
##### 采用scrapy框架抓取，运行文件为run.py，在控制台下直接运行即可，无需在cmd下启动
##### 链家爬取数据部分截图
![](https://github.com/HunterChao/Crawler/blob/master/LianJia/LianJia/lianjia.png)
##### 链家项目的详细介绍请见知乎专栏：https://zhuanlan.zhihu.com/p/25132058?refer=pythoncrawl
### 豆瓣电影信息抓取
##### 按电影分类爬取豆瓣上全部电影信息，共87000余条数据。
##### 包括读取电影分类信息GetPage.py，爬取各类别下电影详情介绍FullContents.py。
##### 豆瓣电影信息的详细介绍请见知乎专栏：https://zhuanlan.zhihu.com/p/24771128?refer=pythoncrawl
