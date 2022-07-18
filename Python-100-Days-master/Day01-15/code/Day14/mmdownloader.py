from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

     def __init__(self, url):
         super().__init__()
         self.url = url

     def run(self):
         filename = self.url[self.url.rfind('/') + 1:]
         resp = requests.get(self.url)
         with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
             f.write(resp.content)


def main():
     # Obtain network resources through the get function of the requests module
     resp = requests.get(
         'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
     # Parse the JSON format data returned by the server into a dictionary
     data_model = resp.json()
     for mm_dict in data_model['newslist']:
         url = mm_dict['picUrl']
         # Realize image download through multi-threading
         DownloadHanlder(url).start()


if __name__ == '__main__':
     main()