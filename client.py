import socket
import threading
import time
from Timeout import input_with_timeout 

class ChatClient:
    def __init__(self) -> None:
        self.addr = ('192.168.115.1', 5050)
        self.server_response = ""
        self.FORMAT = "utf-8"
        
    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect(self.addr)
        
        end = 0
        recv = threading.Thread(target =(self.recv_msg), args =(sock,end))
        recv.start()
        

        if self.server_response == "超過了":
            print("遊戲已滿房")
            sock.close()
            
        if end == 1:
            print("有收到")
            sock.close()
            
    def recv_msg(self,sock,end):
        print("recv連接成功!現在可以接收消息！\n")
        while True:
            try: 
                server_response = sock.recv(4096)
                end = 1
                server_response = server_response.decode(self.FORMAT)
                self.update_response(server_response)
                print(server_response)
                
            except ConnectionResetError:
                print("服務器關閉，聊天已結束！")
                sock.close()
                break
            if self.server_response == "超過了":
                sock.close()
                break
        
            # 開始遊戲從這裡 ↓
            elif self.server_response == "開始遊戲":
                print("3秒後遊戲開始...")
                time.sleep(3)
                self.turn_based(sock,server_response)
                print("client遊戲結束")
                recv = sock.recv(4096).decode(self.FORMAT)
                print(recv)
                end = 1
                time.sleep(5)
                sock.close()
                break
                

    def update_response(self,server_response):
        self.server_response = server_response
        return self.server_response
        
    def turn_based(self,sock,server_response):
        try:
            for round in range(1,6):
                button = 0
                round_time = 0
                print(f"現在是第 {round} 回合", end="\n")
                answer = input_with_timeout(7)
                print(f"answer 是 {answer}, type 是 {type(answer)}")
                special_ans = "Game," + answer
                if answer == "None" or answer == "":
                    special_ans = "Game,None"

                sock.sendall(special_ans.encode(self.FORMAT))
                
                
                server_response = sock.recv(4096)
                server_response = server_response.decode(self.FORMAT)
                

                if server_response == "已收到":
                    print("clientTEST")
                    button = 1
                    first = self.round_player_waiting(sock)[2:6]
                else:
                    pass
                if button == 0:

                    after = server_response[10:14]
                    print(f"這局的答案是 {after}, 這局共得 {self.calculate_score(after)}分")
                    if round == 5:
                        sock.send("遊戲結束".encode(self.FORMAT))
                else:
                    print(f"這局的答案是 {first}, 這局共得 {self.calculate_score(first)}分")
                
                continue
        except:
            print("分數這邊錯誤")
        
            
        

        
            
        
    
    def round_player_waiting(self,sock):
        print("正在等待玩家...")
        # while True:
        
        server_response = sock.recv(4096)
        server_response = server_response.decode(self.FORMAT)
        return server_response

    def calculate_score(self, calculate):
        A_score = int(calculate[0]) * 3       # A是3分、B是1分
        B_score = int(calculate[2])
        return A_score+B_score
    



if __name__ == "__main__":
    client = ChatClient()
    client.connect()
