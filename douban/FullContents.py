# coding=utf-8
# usr/bin/eny python

# Contents 和 Detail 进行合并
# 字段包括： 电影名 导演  主演  片长  类型  评分  评价人数  上映时间   详情链接
import requests
from multiprocessing import Pool,cpu_count
import urllib.request
from lxml import etree
import pymysql.cursors
'''豆瓣内容解读'''

__version__ = '0.0.1'
__author__ = 'Hunter'

tag = urllib.request.quote(u'爱情')
url_1 = 'https://movie.douban.com/tag/{}?start=0&type=T'.format(tag)

class douban(object):
    def __init__(self,*args,**kwargs):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='douban', charset='utf8')
        self.cursor = self.conn.cursor()
        self.sql_info = "INSERT IGNORE INTO `douban_mov` VALUES(%s,%s,%s,%s,%s,%s)"

    def search(self,content):
        '''
        爬取页面内电影信息
        '''
        try:
            selector = etree.HTML(content)
            textslist = selector.xpath('//div[contains(@class,"grid-16-8 clearfix")]/div[1]/div[2]/table')
        except Exception as e:
            print(e)

        try:
            for text in textslist:
                lists = []
                title = text.xpath('tr/td[2]/div/a/text()')     
                score = text.xpath('tr/td[2]/div/div/span[2]/text()')      
                num = text.xpath('tr/td[2]/div/div/span[3]/text()')       
                link = text.xpath('tr/td/a/@href')           
                content = text.xpath('tr/td[2]/div/p/text()')      

                if title:
                    title = title[0].strip().replace('\n', "").replace(' ', "").replace('/', "") if title else ''
                    score = score[0] if score else ''
                    num = num[0].replace('(', "").replace(')', "") if num else ''
                    link = link[0] if link else ''
                    time = content[0].split(' / ')[0] if content else ''
                    actors = content[0].split(' / ')[1:6] if content else ''
                    lists.append({
                        '电影名' : title,
                        '评分' : score,
                        '评价人数' : num,
                        '详情链接' : link,
                        '上映时间' : time,
                        '主演' : actors
                    })
                    if lists:
                        lists = lists.pop()
                    else:
                        lists = u' '

                    print(lists)
                    try:
                        self.cursor.execute(self.sql_info,(str(lists['电影名']),str(lists['评分']),str(lists['评价人数']),str(lists['详情链接']),
                                          str(lists['上映时间']),str(lists['主演'])))
                        self.conn.commit()
                    except Exception as e:
                        print(e)
        except Exception as e:
            pass

