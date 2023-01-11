import threading
import socket
import time
from logstic_decision import logstic

class ChatSever(logstic):
    def __init__(self):
        self.addr = (socket.gethostbyname(socket.gethostname()), 5050)
        super().__init__()
        # self.addr = ("0.0.0.0", 5050)
        self.users = {}
        self.FORMAT = "utf-8"
        self.count_client_ = 0
        self.ans_list = []
        # self.client_ans = {}

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
            # b = 0
            # if len(self.users.values()) == 0 and b == 1:
            #     sock.close()
            #     break

            s, addr = sock.accept()
            self.users[addr] = s
            number = len(self.users)
            
            recv = threading.Thread(target=self.recv_send, args=(s, addr))
            recv.start()

            print(f"用戶{addr}連接成功！現在共有{number}位用戶")
            
            if len(self.users.values()) < 2:
                s.sendall(f"目前人數 {number} 位，正在等待玩家...".encode(self.FORMAT))
            elif len(self.users.values()) > 2:
                s.sendall(f"超過了".encode(self.FORMAT))
                self.users.pop(addr)
                print(f"現在的Client 共有 {len(self.users.keys())}")
                break
            else:
                for client in self.users.values():
                    client.sendall(f"開始遊戲".encode(self.FORMAT))
                    
        
    def recv_send(self, sock, addr):
        while True:
            # 當 超過兩人 break
            if len(self.users.values()) > 2:
                break

            try:  # 測試後發現，當用戶率先選擇退出時，這邊就會報ConnectionResetError
                print("你好 recv")
                # print(self.users)


                # if len(self.users.keys()) == 0:
                #     b = 1
                #     sock.close()
                #     break

                # Server接收的消息傳給所有Client
                # server_send_msg = f"用戶{addr}發來消息：{client_response}"
                # print(server_send_msg)
                # sock.sendall(server_send_msg.encode(self.FORMAT))

                # for client in self.users.values():
                #     client.sendall(server_send_msg.encode(self.FORMAT))
            except ConnectionResetError:
                print(f"用戶{addr}已經退出聊天！")
                self.users.pop(addr)
                for client in self.users.values():
                    client.sendall(f"用戶{addr}已經退出聊天！".encode(self.FORMAT))
                print(f"現在的遊戲室有 {self.users}")
            
            # Server接收消息
            client_response = sock.recv(4096).decode(self.FORMAT)
            
            print(type(client_response))
            print(client_response)
            client_ans = {}
            
            # if client_response.split(",")[0] == "Game":
                # print("瑪瑪我在這")
                
            answer = client_response.split(",")[1]
            try:
                calculate = self.decision(answer)
                print(f"這輪你的分數是 {calculate},")
            except:
                calculate = "0000"
                sock.sendall("輸入有錯,".encode(self.FORMAT))
            self.ans_list.append(answer)
            
            print(f"這裡是ans_list {self.ans_list}")
            if sock not in client_ans:
                client_ans[sock] = client_response
            """
                上面會用到！！！！！！！！！！！！！！！！！！！！
            """
            
            if len(self.ans_list) % 2 == 0:
                
                for client in self.users.values():
                    client.sendall("都準備好了".encode(self.FORMAT))
                    client.sendall(f"這輪你的分數是 {calculate}".encode(self.FORMAT))
                
                
            if len(self.ans_list) % 2 == 1:
                print("True")
                sock.sendall("已收到".encode(self.FORMAT))
                


                print(f"這是測試傳送答案 {client_ans[sock]}")



    # def broadcast(self, client, server_send_msg):
    #     for client in self.users.values():
    #         client.sendall(server_send_msg.encode(self.FORMAT))
                
                
    # def close_sever(self,sock):
    #     for client in self.users.values():
    #         client.close()
    #     sock.close()

    # def count_client(self):
    #     self.count_client_ = len(self.users.keys())
    #     return self.count_client_

if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()