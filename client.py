import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('192.168.115.1', 5050)
s.connect(addr)

def countdown():
    t = 30
    while t:
        # mins, secs = divmod(t, 60)
        
        timer = f"00:{t}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    

def recv_msg():
    print("連接成功！現在可以接收消息！\n")
    while True:
        try: 
            response = s.recv(1024)
            response = response.decode("utf-8")
            print(response)
        except ConnectionResetError:
            print("服務器關閉，聊天已結束！")
            s.close()
        if response == "開始遊戲":
            threading.Thread(target=countdown).start()
        


def send_msg():
    print("連接成功！現在可以發送消息！\n")
    print("輸入esc來退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("utf-8"))

            # ↓為什麼這邊是這樣寫↓
threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()
