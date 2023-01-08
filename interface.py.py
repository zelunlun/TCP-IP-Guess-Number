import pygame
import sys
import time

#各類參數
FPS = 60
sreen_color = 240, 255, 255     #視窗顏色              #R, G, B
width = 500                     #視窗寬度
high = 750                      #視窗高度

bg_color = 200, 230, 255        #畫布顏色
bg_width = width-40             #畫布寬度
bg_high = high                  #畫布高度
test_font = "simhei"

time_num = 30                   #倒數預設值

button_color = 250, 250, 250    #按鈕顏色
bt_text_clr = 0, 0, 0

message_x = 17
message_y = 173
i=0

n = 0
ans = [0]*4                      #輸出數字
message_text =["0000"]*4              #訊息文字
pygame.init()

#創建視窗
screen = pygame.display.set_mode((width, high))
#視窗標題名
pygame.display.set_caption("猜數字對決---")

running = True  #遊戲執行參數 True 即持續開啟


#初始資料
screen.fill((sreen_color))
# 建立畫布
bg = pygame.Surface((bg_width, bg_high))
bg = bg.convert()
bg.fill((bg_color))

#按鈕設置
button_7 = False
bt_7 =[7, bg_width/2-180, 250]                                      #按鈕資訊 [ 數字/指令  , X軸  , Y軸]
font_button = pygame.font.SysFont(test_font, 50)
bt7_text = font_button.render("7", True, bt_text_clr)
bt7_rect = bt7_text.get_rect(center=(bt_7[1]+40, bt_7[2]+40))       #設置文本中心座標

button_4 = False
bt_4 =[4, bg_width/2-180, bt_7[2]+120]
bt4_text = font_button.render("4", True, bt_text_clr)
bt4_rect = bt4_text.get_rect(center=(bt_4[1]+40, bt_4[2]+40))

button_1 = False
bt_1 =[1, bg_width/2-180, bt_4[2]+120]
bt1_text = font_button.render("1", True, bt_text_clr)
bt1_rect = bt1_text.get_rect(center=(bt_1[1]+40, bt_1[2]+40))

button_0 = False
bt_0 =[0, bg_width/2-180, bt_1[2]+120]
bt0_text = font_button.render("0", True, bt_text_clr)
bt0_rect = bt0_text.get_rect(center=(bt_0[1]+40, bt_0[2]+40))

button_8 = False
bt_8 =[8, bg_width/2-40, 250]                                      #按鈕資訊 [ 數字/指令  , X軸  , Y軸]
bt8_text = font_button.render("8", True, bt_text_clr)
bt8_rect = bt8_text.get_rect(center=(bt_8[1]+40, bt_8[2]+40))       #設置文本中心座標

button_5 = False
bt_5 =[5, bg_width/2-40, bt_8[2]+120]
bt5_text = font_button.render("5", True, bt_text_clr)
bt5_rect = bt5_text.get_rect(center=(bt_5[1]+40, bt_5[2]+40))

button_2 = False
bt_2 =[2, bg_width/2-40, bt_5[2]+120]
bt2_text = font_button.render("2", True, bt_text_clr)
bt2_rect = bt2_text.get_rect(center=(bt_2[1]+40, bt_2[2]+40))

button_Ent = False
bt_Ent =[10, bg_width/2-40, bt_2[2]+120]                            #Enter 指令代號10 ( 暫用 )
btEnt_text = font_button.render("Ent", True, bt_text_clr)
btEnt_rect = btEnt_text.get_rect(center=(bt_Ent[1]+40, bt_Ent[2]+40))

button_9 = False
bt_9 =[9, bg_width/2+100, 250]                                      #按鈕資訊 [ 數字/指令  , X軸  , Y軸]
bt9_text = font_button.render("9", True, bt_text_clr)
bt9_rect = bt9_text.get_rect(center=(bt_9[1]+40, bt_9[2]+40))       #設置文本中心座標

button_6 = False
bt_6 =[6, bg_width/2+100, bt_8[2]+120]
bt6_text = font_button.render("6", True, bt_text_clr)
bt6_rect = bt6_text.get_rect(center=(bt_6[1]+40, bt_6[2]+40))

button_3 = False
bt_3 =[3, bg_width/2+100, bt_5[2]+120]
bt3_text = font_button.render("3", True, bt_text_clr)
bt3_rect = bt3_text.get_rect(center=(bt_3[1]+40, bt_3[2]+40))

button_Del = False
bt_Del =[11, bg_width/2+100, bt_2[2]+120]                            #Delete 指令代號11 ( 暫用 )
btDel_text = font_button.render("Del", True, bt_text_clr)
btDel_rect = btDel_text.get_rect(center=(bt_Del[1]+40, bt_Del[2]+40))


#text_1 = font_0.render("1", True, (255, 0, 0))

def restart_bg():
    bg.fill((bg_color))                                             #清空畫布
    #導入戰敗圖
    image_fail = pygame.image.load("C:\TCP_IP專題\戰敗.png")       #visual code 需附上圖片完整位址
    image_fail.convert()
    bg.blit(image_fail, (bg_width - 40*1, 0))
    #導入勝利圖
    image_win = pygame.image.load("C:\TCP_IP專題\勝利.png")        #visual code 需附上圖片完整位址
    image_win.convert()
    bg.blit(image_win, (bg_width - 40*3, 0))
    #導入回合圖
    image_round = pygame.image.load("C:\TCP_IP專題\回合.png")      #visual code 需附上圖片完整位址
    image_round.convert()
    bg.blit(image_round, (bg_width - 40*5, 0))
    #繪製分割線
    pygame.draw.rect(bg, (0, 0, 0), [0, 43, bg_width, 2], 0)
    
    #繪製資訊窗口
    pygame.draw.rect(bg, (255, 255, 255), [10, 49, bg_width-20, 160], 0)
    pygame.draw.rect(bg, (0, 0, 0), [10, 49, bg_width-20, 160], 2)              #窗口邊界
    
    #繪製按鈕
    pygame.draw.rect(bg, button_color, [bt_7[1], bt_7[2], 80, 80], 0)           #按鈕圖形       #按鈕 7
    pygame.draw.rect(bg, (200, 200, 200), [bt_7[1], bt_7[2], 80, 80], 4)        #按鈕邊界
    bg.blit(bt7_text, bt7_rect)                                                 #按鈕文字
    pygame.draw.rect(bg, button_color, [bt_4[1], bt_4[2], 80, 80], 0)                          #按鈕 4
    pygame.draw.rect(bg, (200, 200, 200), [bt_4[1], bt_4[2], 80, 80], 4)
    bg.blit(bt4_text, bt4_rect)
    pygame.draw.rect(bg, button_color, [bt_1[1], bt_1[2], 80, 80], 0)                          #按鈕 1
    pygame.draw.rect(bg, (200, 200, 200), [bt_1[1], bt_1[2], 80, 80], 4)
    bg.blit(bt1_text, bt1_rect)
    pygame.draw.rect(bg, button_color, [bt_0[1], bt_0[2], 80, 80], 0)                          #按鈕 0
    pygame.draw.rect(bg, (200, 200, 200), [bt_0[1], bt_0[2], 80, 80], 4)
    bg.blit(bt0_text, bt0_rect)
    pygame.draw.rect(bg, button_color, [bt_8[1], bt_8[2], 80, 80], 0)           #按鈕圖形       #按鈕 8
    pygame.draw.rect(bg, (200, 200, 200), [bt_8[1], bt_8[2], 80, 80], 4)        #按鈕邊界
    bg.blit(bt8_text, bt8_rect)                                                 #按鈕文字
    pygame.draw.rect(bg, button_color, [bt_5[1], bt_5[2], 80, 80], 0)                          #按鈕 5
    pygame.draw.rect(bg, (200, 200, 200), [bt_5[1], bt_5[2], 80, 80], 4)
    bg.blit(bt5_text, bt5_rect)
    pygame.draw.rect(bg, button_color, [bt_2[1], bt_2[2], 80, 80], 0)                          #按鈕 2
    pygame.draw.rect(bg, (200, 200, 200), [bt_2[1], bt_2[2], 80, 80], 4)
    bg.blit(bt2_text, bt2_rect)
    pygame.draw.rect(bg, (80, 255, 80), [bt_Ent[1], bt_Ent[2], 80, 80], 0)                    #按鈕 Enter
    pygame.draw.rect(bg, (80, 180, 80), [bt_Ent[1], bt_Ent[2], 80, 80], 4)
    bg.blit(btEnt_text, btEnt_rect)
    pygame.draw.rect(bg, button_color, [bt_9[1], bt_9[2], 80, 80], 0)           #按鈕圖形       #按鈕 9
    pygame.draw.rect(bg, (200, 200, 200), [bt_9[1], bt_9[2], 80, 80], 4)        #按鈕邊界
    bg.blit(bt9_text, bt9_rect)                                                 #按鈕文字
    pygame.draw.rect(bg, button_color, [bt_6[1], bt_6[2], 80, 80], 0)                          #按鈕 6
    pygame.draw.rect(bg, (200, 200, 200), [bt_6[1], bt_6[2], 80, 80], 4)
    bg.blit(bt6_text, bt6_rect)
    pygame.draw.rect(bg, button_color, [bt_3[1], bt_3[2], 80, 80], 0)                          #按鈕 3
    pygame.draw.rect(bg, (200, 200, 200), [bt_3[1], bt_3[2], 80, 80], 4)
    bg.blit(bt3_text, bt3_rect)
    pygame.draw.rect(bg, (255, 80, 80), [bt_Del[1], bt_Del[2], 80, 80], 0)                      #按鈕 Delete
    pygame.draw.rect(bg, (180, 80, 80), [bt_Del[1], bt_Del[2], 80, 80], 4)
    bg.blit(btDel_text, btDel_rect)
    
#倒數計時
def time_down(time_num):
    time_num -= 1
    time.sleep(1)
    return time_num

#按鈕判斷
def button_check(n, c_x, c_y):
    #print(x, y)
    #print(n)
    if(bt_0[1]+20 <= c_x <= bt_0[1]+100 and bt_0[2]<= c_y <= bt_0[2]+80 ):                #判斷是不是按到 0
        print(bt_0[0],"被按到")
        ans[n] = 0
        return 1
    elif(bt_1[1]+20 <= c_x <= bt_1[1]+100 and bt_1[2]<= c_y <= bt_1[2]+80 ):              #判斷是不是按到 1
        print(bt_1[0],"被按到")
        ans[n] = 1
        return 1
    elif(bt_2[1]+20 <= c_x <= bt_2[1]+100 and bt_2[2]<= c_y <= bt_2[2]+80 ):              #判斷是不是按到 2
        print(bt_2[0],"被按到")
        ans[n] = 2
        return 1
    elif(bt_3[1]+20 <= c_x <= bt_3[1]+100 and bt_3[2]<= c_y <= bt_3[2]+80 ):              #判斷是不是按到 3
        print(bt_3[0],"被按到")
        ans[n] = 3
        return 1
    elif(bt_4[1]+20 <= c_x <= bt_4[1]+100 and bt_4[2]<= c_y <= bt_4[2]+80 ):              #判斷是不是按到 4
        print(bt_4[0],"被按到")
        ans[n] = 4
        return 1
    elif(bt_5[1]+20 <= c_x <= bt_5[1]+100 and bt_5[2]<= c_y <= bt_5[2]+80 ):              #判斷是不是按到 5
        print(bt_5[0],"被按到")
        ans[n] = 5
        return 1
    elif(bt_6[1]+20 <= c_x <= bt_6[1]+100 and bt_6[2]<= c_y <= bt_6[2]+80 ):              #判斷是不是按到 6
        print(bt_6[0],"被按到")
        ans[n] = 6
        return 1
    elif(bt_7[1]+20 <= c_x <= bt_7[1]+100 and bt_7[2]<= c_y <= bt_7[2]+80 ):              #判斷是不是按到 7
        print(bt_7[0],"被按到")
        ans[n] = 7
        return 1
    elif(bt_8[1]+20 <= c_x <= bt_8[1]+100 and bt_8[2]<= c_y <= bt_8[2]+80 ):              #判斷是不是按到 8
        print(bt_8[0],"被按到")
        ans[n] = 8
        return 1
    elif(bt_9[1]+20 <= c_x <= bt_9[1]+100 and bt_9[2]<= c_y <= bt_9[2]+80 ):              #判斷是不是按到 9
        print(bt_9[0],"被按到")
        ans[n] = 9
        return 1
    else:
        print("什麼都沒按到")
        return 0

#按鈕指令判斷
def bt_sys(c_x, c_y):
    if(bt_Ent[1]+20 <= c_x <= bt_Ent[1]+100 and bt_Ent[2]<= c_y <= bt_Ent[2]+80 ):       #判斷是不是按到 Enter
        print("Enter ","被按到")
        return 1
    elif(bt_Del[1]+20 <= c_x <= bt_Del[1]+100 and bt_Del[2]<= c_y <= bt_Del[2]+80 ):      #判斷是不是按到 Delete
        print("Delete ","被按到")
        return 0

#遊戲迴圈---動態資料
while running:
    pygame.time.Clock().tick(FPS)            # 1 秒內僅能執行 10 次，用於限制 while 速度

#取得輸入
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_0 = True
            x, y =event.pos                     # 捕抓鼠標在 sreen 上的座標
            #print(ans, i)
            if(bt_sys(x, y) == 0):              # 判斷是否刪除 ans 並重製 n
                for j in range(4): ans[j] = 0
                n = 0
            elif(bt_sys(x, y) == 1):
                '''
                if(i < 3):
                    i += 1
                for k in range(i, 0, -1):
                    message_text[i] = message_text[i-1]
                for j in range(4): ans[j] = 0
                n = 0
                '''
            if n <= 3:
                n += button_check(n, x, y)  
                #n = n+1
                #print(ans, i)
            
        if event.type == pygame.QUIT:           #判斷 even 是不是觸發條件來關閉視窗
            running = False

    
#更新遊戲
    question = "1234"
    fail = "1"
    win = "2"
    round = "3"

    if(time_num <= 0):
        time_num = 30
    time_num = time_down(time_num)
    message_text[i] = str(ans[0]) + str(ans[1]) + str(ans[2]) + str(ans[3])

    
    

#畫面顯示
    restart_bg()                          #背景初始化
    # 題目文本
    font_question = pygame.font.SysFont(test_font, 59)
    text_question = font_question.render(question, True, (0, 0, 255), (bg_color))  # 文本內容
    question_rect = text_question.get_rect(center=(bg_width/6, 23))
    bg.blit(text_question, question_rect)

    # 戰敗數文本
    font_fail = pygame.font.SysFont(test_font, 59)
    text_fail = font_fail.render(fail, True, (150, 0, 255), (bg_color))  # 文本內容
    fail_rect = text_fail.get_rect(center=(bg_width-60, 23))
    bg.blit(text_fail, fail_rect)

    # 勝利數文本
    font_win = pygame.font.SysFont(test_font, 59)
    text_win = font_win.render(win, True, (255, 200, 0), (bg_color))  # 文本內容
    win_rect = text_win.get_rect(center=(bg_width-140, 23))
    bg.blit(text_win, win_rect)

    # 回合數文本
    font_round = pygame.font.SysFont(test_font, 59)
    text_round = font_round.render(round, True, (120, 120, 120), (bg_color))  # 文本內容
    round_rect = text_round.get_rect(center=(bg_width-220, 23))
    bg.blit(text_round, round_rect)

    # 倒數計時文本
    font_time = pygame.font.SysFont(test_font, 59)
    if(time_num < 100):
        down_num = str(time_num)
        text_time = font_time.render(str(time_num), True, (255, 0, 0), (255, 255, 255))  # 文本內容
    if(time_num < 10):
        down_num = "0" + str(time_num)
        text_time = font_time.render(down_num, True, (255, 0, 0), (255, 255, 255))  # 文本內容
    bg.blit(text_time, (bg_width-60, 57))

    
    # 資訊窗文本
    font_message = pygame.font.SysFont(message_text,50)
    text_message = font_message.render(message_text[0], True, (0, 0, 0), (255, 255, 255))  # 文本內容
    bg.blit(text_message, (message_x ,message_y))
    font_message = pygame.font.SysFont(message_text,50)
    text_message = font_message.render(message_text[1], True, (0, 0, 0), (255, 255, 255))  # 文本內容
    bg.blit(text_message, (message_x ,message_y-40))
    font_message = pygame.font.SysFont(message_text,50)
    text_message = font_message.render(message_text[2], True, (0, 0, 0), (255, 255, 255))  # 文本內容
    bg.blit(text_message, (message_x ,message_y-80))
    font_message = pygame.font.SysFont(message_text,50)
    text_message = font_message.render(message_text[3], True, (0, 0, 0), (255, 255, 255))  # 文本內容
    bg.blit(text_message, (message_x ,message_y-120))

    #顯示畫布
    screen.blit(bg, ((width-bg_width)/2, 0))
    #更新資料
    pygame.display.update()

pygame.quit()