# import socket

# class ChatClient:
#     def __init__(self) -> None:
#         self.addr = ('192.168.115.1', 5050)
#         self.server_response = ""
#         self.FORMAT = "utf-8"
#     def connect(self):
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         sock.connect(self.addr)

# if __name__ == "__main__":
#     client = ChatClient()
#     client.connect()

# a = "1234"

# print([x for x in a])

a = {
    "A":0, "B":2, "C":1
}

# for i in sorted(a.values()):
#     print(i)

print(a[0])
