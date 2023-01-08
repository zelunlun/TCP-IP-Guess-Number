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
                server_response = sock.recv(1024)
                server_response = server_response.decode("utf-8")
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
                self.turn_based()
                
                sock.close()

    def update_response(self,server_response):
        self.server_response = server_response
        return self.server_response
        
    def turn_based(self):
        for round in range(1,6):
            round_time = 0
            print(f"現在是第 {round} 回合")
            self.Gamestart()
            # count_time = threading.Thread(target =(self.count_time), args=(round_time,))
            # start = threading.Thread(target=(self.Gamestart), args=(round_time,))   # ,args=()
            # start.setDaemon(True)
            # start.start()
            # count_time.start()
        
            
        
    def Gamestart(self):
        while True:
            ans = input_with_timeout("", 5)
            return ans
            # if round_time == 30:
            #     break
            # elif client_send_msg != None:
            #     break
    
    # def count_time(self, round_time):
    #     while True:
    #         time.sleep(1)
    #         round_time += 1
    #         if round_time ==30:
    #             break



if __name__ == "__main__":
    client = ChatClient()
    client.connect()


    # t = 30
    # while t:
    #     # mins, secs = divmod(t, 60)
        
    #     timer = f"00:{t}"
    #     print(timer, end="\r")
    #     time.sleep(1)
    #     t -= 1