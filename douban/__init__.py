# coding=utf-8
# usr/bin/eny python

from douban_project.GetPage import theme_page
from douban_project.FullContents import douban
from multiprocessing import Pool,cpu_count
import threading
import urllib.request
import time
import requests


page_infos = theme_page()
page_infos = page_infos.get_total_num()    # 主题&页数
# pool = Pool(cpu_count())
run = douban()


for page_info in page_infos:   # 遍历所有主题
    tags = page_info['主题']
    page = page_info['总页数']
    tag = urllib.request.quote(tags)
    threads = []
    for i in range(int(page)):    # 每个主题下的所有页数
        if i == 0:
            url = 'https://movie.douban.com/tag/{0}?start={1}&type=T'.format(tag, 0)
        else:
            url = 'https://movie.douban.com/tag/{0}?start={1}&type=T'.format(tag, i * 20)
        s = requests.get(url)
        s = s.content.decode('utf-8')
        # pool.apply_async(run.search(s))
        # pool.close()
        # pool.join()
        lists = run.search(s)
        print('--------------------------------------------------------------')
        time.sleep(5)
