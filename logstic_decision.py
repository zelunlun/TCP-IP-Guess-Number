# ans = [int(z) for z in input()] # 題目
# N = [int(s) for s in input()]   # 輸入的數字

class logstic():
    def __init__(self) -> None:
        self.answer = [x for x in "1234"]
    def decision(self,answer):
        # times=1
        # while 1==1:
        a_count = 0
        b_count = 0
        for i in range (4):
            for j in range (4):
                if self.answer[i] == answer[j] and i==j:a_count+=1
                if self.answer[i] == answer[j] and i!=j:b_count+=1
        return f"{a_count}A{b_count}B"



#   if a == 4 :
#     print ('You win with',times,'times')
#     break
#   N = [int(s) for s in input()]
#   a = 0
#   b = 0
#   times += 1