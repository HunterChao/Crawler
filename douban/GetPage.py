# coding=utf-8
# usr/bin/eny python

import urllib.request
import requests
from lxml import etree
import time
'''
获取每个主题下有多少页内容  (没有输入，输出字典)
'''
class theme_page(object):
    def __init__(self):
        self.tags = [u"爱情", u"喜剧", u"动画", u'剧情', u'科幻', u'动作', u'经典', u'悬疑', u'青春', u'犯罪', u'惊悚', \
                u"文艺", u"搞笑", u"纪录片", u'励志', u'恐怖', u'战争', u'短片', u'黑色幽默', u'魔幻', u'传记', \
                u'情色', u"感人", u"暴力", u'动画短片', u'家庭', u'音乐', u'童年', u'浪漫', u'黑帮', u'女性', \
                u'同志', u"史诗", u"童话", u'烂片', u'cult']

    def get_total_num(self):
        tags = self.tags
        total_num = []
        list = []
        for tag in tags:
            # print(tag)   #主题名称
            re_url = 'https://movie.douban.com/tag/{}?start=0&type=T'.format(urllib.request.quote(tag))
            # print(re_url)     # 主题链接
            s = requests.get(re_url)
            contents = s.content.decode('utf-8')
            selector = etree.HTML(contents)
            num = selector.xpath('//*[@id="content"]/div/div[1]/div[3]/a[10]/text()')
            total_num.append(int(num[0]))
            # print(num[0])    # 总页数
            list.append({                # list :{'爱情': '393'}, {'喜剧': '392'}, {'动画': '274'},
                '主题' : tag ,
                '总页数' : num[0]
            })
        return list
# if __name__ == '__main__':
#     run = theme_page()
#     run = run.get_total_num()
#     print(run)


    # total_num = sum(run)
    # print(total_num)
    # print('https://movie.douban.com/tag/{}?start=0&type=T'.format(urllib.request.quote(u'喜剧')))
    # 共 5141个页面