import logging
import os.path as osp
from argparse import ArgumentParser
from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BaiduImageCrawler
from icrawler.builtin import BingImageCrawler


google_storage = {'root_dir': 'data/anne_mariegoogle'}
google_crawler = GoogleImageCrawler(parser_threads=4,
                                    downloader_threads=4,
                                    storage = google_storage)
google_crawler.crawl(keyword='anne marie',
                    max_num=1000)

#baidu_storage = {'root_dir': 'data/anne_mariebaidu'}
#baidu_crawler = BaiduImageCrawler(parser_threads=4,
#                                    downloader_threads=4,
#                                    storage = baidu_storage)
#baidu_crawler.crawl(keyword='anne marie',
#                    max_num=1000)
