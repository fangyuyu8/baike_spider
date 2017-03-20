# _*_ coding:utf-8 _*_
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        #print('下载的页面：', response.read())
        return response.read()


