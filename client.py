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
        
        recv = threading.Thread(target =(self.recv_msg), args =(sock,))
        recv.start()
        
        while True:
            # print(f"send response 是 {self.server_response }")
            if self.server_response == "超過了":
                print("遊戲已滿房")
                sock.close()
                break
            # client_send_msg = input()
            # if client_send_msg == "esc":
            #     print("你退出了聊天")
            #     sock.close()
            #     break
            # else:
            #     sock.sendall(client_send_msg.encode(self.FORMAT))

    def recv_msg(self,sock):
        print("recv連接成功!現在可以接收消息！\n")
        while True:
            try: 
                server_response = sock.recv(4096)
                server_response = server_response.decode(self.FORMAT)
                self.update_response(server_response)
                print(server_response)
                # print(f"recv 的 response 是 {self.server_response}")

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
                sock.close()
                break
                

    def update_response(self,server_response):
        self.server_response = server_response
        return self.server_response
        
    def turn_based(self,sock,server_response):
        try:
            for round in range(1,6):
                round_time = 0
                print(f"現在是第 {round} 回合", end="\n")
                answer = self.Gamestart()
                print(f"answer 是 {answer}, type 是 {type(answer)}")
                special_ans = "Game," + answer
                if answer == "None" or answer == "":
                    special_ans = "Game,None"

                sock.sendall(special_ans.encode(self.FORMAT))
                
                
                server_response = sock.recv(4096)
                server_response = server_response.decode(self.FORMAT)
                print(f"server_res 是 {server_response} ")

                if server_response == "已收到":
                    print("clientTEST")
                    self.round_player_waiting(sock)
                elif server_response == "都準備好了":
                    print(f"server_response是{server_response}")
                    continue
                # count_time = threading.Thread(target =(self.count_time), args=(round_time,))
                # start = threading.Thread(target=(self.Gamestart), args=(round_time,))   # ,args=()
                # start.setDaemon(True)
                # start.start()
                # count_time.start()
        except:
            print("分數這邊錯誤")
        
            
        

        
            
        
    def Gamestart(self):
        while True:
            ans = input_with_timeout("", 15)
            return ans
            # if round_time == 30:
            #     break
            # elif client_send_msg != None:
            #     break
    
    def round_player_waiting(self,sock):
        print("正在等待玩家...")
        while True:
            
            server_response = sock.recv(4096)
            server_response = server_response.decode(self.FORMAT)
            print(f"ser {server_response}")
            if server_response == "都準備好了":
                break
    # def count_time(self, round_time):
    #     while True:
    #         time.sleep(1)
    #         round_time += 1
    #         if round_time ==30:
    #             break



if __name__ == "__main__":
    client = ChatClient()
    client.connect()
