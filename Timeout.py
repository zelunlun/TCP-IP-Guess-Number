import threading
import queue
import sys

def get_input(channel):
    response = input()
    channel.put(response)


def input_with_timeout(timeout):
    channel = queue.Queue()
    thread = threading.Thread(target=get_input, args=(channel,))
    # by setting this as a daemon thread, python won't wait for it to complete
    thread.daemon = True
    thread.start()

    try:
        response = channel.get(True, timeout)
        # print(f"{response}, {type(response)}, channel = {channel}")
        
        return response
    except queue.Empty:
        # print(channel)
        pass
    return str(None)
    


if __name__ == "__main__":
    

    a = input_with_timeout(6)
    print(a)




# # # # import the time module
# # import time
  
# # # # define the countdown func.
# # # def countdown(t):
    
# # #     while t:
# # #         mins, secs = divmod(t, 60)
# # #         print(mins,secs)
# # #         # timer = '{:02d}:{:02d}'.format(mins, secs)
# # #         # print(timer, end="\r")
# # #         # time.sleep(1)
# # #         # t -= 1
      
# # #     print('Fire in the hole!!')
  
  
# # # # input time in seconds
# # # t = input("Enter the time in seconds: ")
  
# # # # function call
# # # countdown(int(t))

# # for i in range(1,5):
# #     print(f"第 {i} 個回合")

    
# #     if True:    # if 傳送訊息（答案）時
# #         s.sendall()   # 送一個傳送完了的Text



# # """
# #     要如何讓A or B等待?
# #     1. 用計時器 ( moudle ) 來累積時間
# #     2. 用time 的 sleep function?
    
# # """


# #     # time.sleep(1)
# #     # if i <= 10:
# #     #     print(f"時間快到嘍，還剩下 {i} 秒")

# # import json
# # dict_ = '{"A":1, "B":2}'
# # print(type(dict_))
# # dict_ = json.loads(dict_)
# # print(type(dict_))

# import threading, time

# round_time = 0

# # def count_time(round_time):
# #     # lock.acquire()
# #     while True:
# #         print(f"這是第一個的第 {round_time} 秒")
# #         time.sleep(1)
# #         round_time += 1
# #         if round_time ==10:
# #             # lock.release()
# #             break
    
# def count_time2(round_time):
#     while True:
#         # lock.acquire()
        
#         if round_time == 5:
#             # lock.release()
#             break
#         n = input()

#         if n != None:
#             break

        
# while True:
#         print(f"這是第一個的第 {round_time} 秒")
#         time.sleep(1)
#         round_time += 1
#         if round_time ==10:
#             # lock.release()
#             break

# # for round in range(1,6):
# round_time = 0
# # print(f"現在是第 {round} 回合")
# lock = threading.Lock()
# # count_time_ = threading.Thread(target =(count_time), args=(round_time,))
# start = threading.Thread(target=(count_time2), args=(round_time,))   # ,args=()
# start.setDaemon=True
# start.start()
# # count_time_.start()
# # start.join()