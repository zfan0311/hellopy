import os
import hashlib
import re

import ssl
import urllib.request

__all__ = ['rss']

ssl._create_default_https_context = ssl._create_unverified_context

class Resource():

    def __init__(self, path="download"):
        """ 设置保存路径 """
        self.path = path
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    def get(self, url):
        if not self.is_url(url):
            return url

        filename = self.md5_8_name(url)
        fullname =  '{}{}{}'.format(self.path, os.sep, filename)

        if not os.path.exists(fullname):
            self.download(url, fullname)

        return fullname

    def md5_8_name(self, url):
        """ 把下载的文件重命名为地址的md5前8位 """
        m = hashlib.md5()
        m.update(url.encode('utf-8'))
        return m.hexdigest()[:8] + os.path.splitext(url)[1]

    def download(self, url, fullname):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        print("Downloading: " + url)
        # urllib.request.urlretrieve(url, filename=fullname)
        urllib.request.urlretrieve(url, fullname)
        # with urllib.request.urlopen(, context=self.ctx) as u, \
        #     open(, 'wb') as f:
        #     f.write(u.read())

    def is_url(self, url):
        regex = re.compile(
                r'^(?:http|ftp)s?://' # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
                r'localhost|' #localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
                r'(?::\d+)?' # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

rss = Resource()