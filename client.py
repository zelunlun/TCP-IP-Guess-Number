import socket
import threading
import time

class ChatClient:
    def __init__(self) -> None:
        self.addr = ('192.168.115.1', 5050)
        self.recv_fromserver = {"text":None, }
        self.FORMAT = "utf-8"
    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.addr)

        print("send 連接成功！現在可以發送消息！\n")
        while True:
            if self.recv_fromserver["text"] == "超過了":
                print("遊戲已滿房")
                break
            client_send_msg = input()
            if client_send_msg == "esc":
                print("你退出了聊天")
                sock.close()
                break
            recv = threading.Thread(target=self.recv_msg, args=(sock,))
            recv.start()

            sock.send(client_send_msg.encode("utf-8")) # self.FORMAT

    def recv_msg(self):
        print("recv連接成功!現在可以接收消息！\n")
        while True:
            try: 
                recv_fromserver = self.sock.recv(1024)
                recv_fromserver = recv_fromserver.decode("utf-8")
                self.update_response(recv_fromserver)
                
            except ConnectionResetError:
                print("服務器關閉，聊天已結束！")
                self.sock.close()
            if self.recv_fromserver == "超過了":
                break
            print(recv_fromserver)
        # if response == "開始遊戲":
        #     threading.Thread(target=countdown).start()
        
    def update_response(self,recv_fromserver):
        self.recv_fromserver = recv_fromserver
        return self.recv_fromserver
        
    def countdown():
        t = 30
        while t:
            # mins, secs = divmod(t, 60)
            
            timer = f"00:{t}"
            print(timer, end="\r")
            time.sleep(1)
            t -= 1



if __name__ == "__main__":
    client = ChatClient()
    client.connect()
    # threads = [, threading.Thread(target=client.send_msg)]
    # for t in threads:
    #     t.start()


            # ↓為什麼這邊是這樣寫↓

