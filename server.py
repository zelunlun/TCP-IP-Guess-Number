import threading
import socket

import time


class ChatSever:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        try:
            self.sock.bind(self.addr)
        except:
            print('Error!')    
        self.sock.listen(2)
        print("服務器已開啓，等待連接...")
        # self.IstwoPlayer()
        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print(f"用戶{addr}連接成功！現在共有{number}位用戶")
            if len(self.users.values()) < 2:
                s.sendall(f"目前人數 {number} 位，正在等待玩家...".encode(self.FORMAT))
            elif len(self.users.values()) > 2:
                s.sendall("超過了".encode(self.FORMAT))
                self.users.pop(addr)
                print(f"現在的Client 共有 {len(self.users.keys())}")
            else:
                for client in self.users.values():
                    client.sendall(f"開始遊戲".encode(self.FORMAT))
                threading.Thread(target=self.recv_send, args=(s, addr)).start()
        
    def recv_send(self, sock, addr):
        while True:
            try:  # 測試後發現，當用戶率先選擇退出時，這邊就會報ConnectionResetError
                print("你好 recv")
                print(self.users)
                client_response = sock.recv(4096).decode(self.FORMAT)
                msg = f"用戶{addr}發來消息：{client_response}"
                print(msg)
                for client in self.users.values():
                    client.sendall(msg.encode(self.FORMAT))
            except ConnectionResetError:
                print(f"用戶{addr}已經退出聊天！")
                self.users.pop(addr)
                for client in self.users.values():
                    client.sendall(f"用戶{addr}已經退出聊天！".encode(self.FORMAT))
    
    
    # def exit_game(self, msg, addr):
    #     if msg == "esc":
    #         print(f"用戶{addr}已經退出聊天！")
    #         self.users.pop(addr)
    #         for client in self.users.values():
    #             client.sendall(f"用戶{addr}已經退出聊天！".encode(self.FORMAT))
            
    def broadcast(self, client, msg):
        for client in self.users.values():
            client.sendall(msg.encode(self.FORMAT))
                
                
    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
    
    def countdown(self):
        t = 30
        while t:
            # mins, secs = divmod(t, 60)
            timer = f"00:{t}"
            self.sock.sendall
            time.sleep(1)
            t -= 1

    def count_client(self):
        self.__count_client = len(self.users.keys())
        return self.__count_client

if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()