"""
ftp 文件服务器 服务端
多进程/多线程并发 socket
"""
from socket import *
from threading import Thread
import sys

HOST = '0.0.0.0'
PORT = 8848
ADDR = (HOST,PORT)
FTP = "/home/tarena/FTP/" # 文件库位置

# 实现具体功能
class FtpServer(Thread):
    """
    查看文件列表，上传，下载，退出
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def run(self):
        while True:
            data = self.connfd.recv(1024).deconde()
            if data[0]=='Q' or not data:
                return





# 搭建网络并发模型
def main():
    # 创建套接字
    s = socket()
    s.bind(ADDR)
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    while True:
        try:
            c,addr = s.accept()
            print('Connect from ',addr)
        except KeyboardInterrupt as e:
            sys.exit('服务出错')
        except Exception as e:
            print(e)
            continue

        f = FtpServer(c)
        f.setDaemon(True)
        f.start()


if __name__ == '__main__':
   main()