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
        self.AB = []
        self.total_scores = {}
        self.compare_list = []
            

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
            round_count = 1
            # 當 超過兩人 break
            if len(self.users.values()) > 2:
                break

            try:  
                pass
            except ConnectionResetError:
                print(f"用戶{addr}已經退出聊天！")
                self.users.pop(addr)
                for client in self.users.values():
                    client.sendall(f"用戶{addr}已經退出聊天！".encode(self.FORMAT))
                print(f"現在的遊戲室有 {self.users}")
            
            # Server接收消息
            client_ans = {}
            client_response = sock.recv(4096).decode(self.FORMAT)
            
            

            if client_response == "遊戲結束":
                for i in sorted(self.total_scores.values()):
                    self.compare_list.append(i)
                    com_dict = {v : k for k, v in self.total_scores.items()}
                    if len(self.compare_list) >= 2:
                        if self.compare_list[0] == self.compare_list[1]:
                            for client in self.users.values():
                                client.send("雙方平手!".encode(self.FORMAT))
                            sock.close()
                            break
                        else:
                            for client in self.users.values():
                                client.send(f"獲勝的是{com_dict[i]}".encode(self.FORMAT))
                            sock.close()
                            break
            
            
            try :
                answer = client_response.split(",")[1]              # 這是給的答案 (數字)
            except:
                print("遊戲結束")
                break
            
            try:
                calculate = self.decision(answer)               # 算出幾A幾B   
                round_score = self.calculate_score(calculate)   # 算出本輪分數
                if sock not in self.total_scores:
                    self.total_scores[sock] = round_score
                else:
                    self.total_scores[sock] += round_score
                
            except:
                calculate = "0A0B"
                sock.sendall("輸入有錯,".encode(self.FORMAT))
            
            self.ans_list.append(answer)                        # ans_list是用來判斷
                                                                # 是否都準備  
            if sock not in client_ans:
                client_ans[sock] = client_response
            """
                上面會用到！！！！！！！！！！！！！！！！！！！！
            """
            self.AB.append(calculate)

            if len(self.ans_list) % 2 == 0:
                
                for client in self.users.values():
                    client.sendall(f"{self.AB}".encode(self.FORMAT))
                
                    
                    
                self.AB.pop()
                self.AB.pop()
            if len(self.ans_list) % 2 == 1:
                sock.sendall("已收到".encode(self.FORMAT))
            
                
           

    def calculate_score(self, calculate):
        A_score = int(calculate[0]) * 3       # A是3分、B是1分
        B_score = int(calculate[2])
        return A_score+B_score


    
if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()