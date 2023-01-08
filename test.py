# from Timeout import input_with_timeout

# ans =input_with_timeout("",3)
# print(ans)
import threading
import socket
import time

class ChatSever:
    def __init__(self):
        self.addr = (socket.gethostbyname(socket.gethostname()), 5050)
        self.users = {}
        self.FORMAT = "utf-8"
        self.answer = "1234"
        self.__count_client = 0

    # def IstwoPlayer(self):
    #     print("正在等待玩家...")
    #     while True:
    #         if len(self.users.keys()) == 2:
    #             self.accept_cont()
            

    def start_sever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(self.addr)
        except:
            print('Error!')    
        sock.listen(2)
        print("服務器已開啓，等待連接...")
        # self.IstwoPlayer()
        self.accept_cont(sock)

    def accept_cont(self,sock):
        while True:
            s, addr = sock.accept()
            print(s)
if __name__ == "__main__":
    server = ChatSever()
    server.start_sever()
        