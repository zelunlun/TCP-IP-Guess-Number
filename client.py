import socket
import threading
import time

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
            client_send_msg = input()
            if client_send_msg == "esc":
                print("你退出了聊天")
                sock.close()
                break
            else:
                sock.sendall(client_send_msg.encode(self.FORMAT))

    def recv_msg(self,sock):
        print("recv連接成功!現在可以接收消息！\n")
        while True:
            try: 
                server_response = sock.recv(1024)
                server_response = server_response.decode("utf-8")
                self.update_response(server_response)
                # print(f"recv 的 response 是 {self.server_response}")

            except ConnectionResetError:
                print("服務器關閉，聊天已結束！")
                sock.close()
                break
            if self.server_response == "超過了":
                sock.close()
                break
            print(server_response)
        # if response == "開始遊戲":
        #     threading.Thread(target=countdown).start()    
    

    def update_response(self,server_response):
        self.server_response = server_response
        return self.server_response
        
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


            # ↓為什麼這邊是這樣寫↓

