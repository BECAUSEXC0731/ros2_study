#学习知识：多线程和节点的基本创建使用
#功能：下载指定url的内容，并统计内容长度



import threading
import requests


class download:
    def download(self,url,callback_count):
        print("start download")
        response=requests.get(url)
        response.encoding="utf-8"
        callback_count(url,response.text)

    def start_download(self,url,callback_count):
        thread=threading.Thread(target=self.download,args=(url,callback_count))
        thread.start()



def count(url, content):
    print(f"{url} download success, the content length is {len(content)}")


def main():
    download1=download()
    download1.start_download("https://www.qidian.com/chapter/1035420986/730944635/",count)
     
    
