import random
#1. 請輸入遊戲人數
#2. 建立好終極密碼
#3. 1號玩家請輸入
# "大於" 30小於"100"
#4. 2號玩家請輸入 小於30大於100的數字
print("請輸入玩家人數: ")
players = int(input())
#print(type(player))
print("您輸入的玩家人數:" + str(players) + "人")
final_num = random.randint(1,100)
#等等殺掉
print(final_num)
max_num = 100
min_num = 1
#while
#要加1

player_answer = 0
isEnd = True
while isEnd:
    for player in range(1,players + 1):
        print("玩家"+ str(player) + "請輸入大於" + str(min_num) + "和小於" + str(max_num) + "的正整數")
        player_answer = int(input())
        if player_answer > final_num:
            max_num = player_answer 
        elif player_answer < max_num :
            min_num = player_answer
        if final_num == player_answer :
            print("玩家"+ str(player) + "猜中密碼")
            isEnd = False
            break
        
    
        