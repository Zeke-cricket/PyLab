import random
player_answer = 0
print("輸入的玩家人數:")
class GuessGame:
    def __init__(self, max_num, min_num):
        self.max_num = max_num
        self.min_num = min_num
        self.final_num = random.randint(self.min_num, self.max_num)
        self.players = int(input())
    def runguess(self):
        print("您輸入的玩家人數:" + str(self.players) + "人")
        print(self.final_num)
        isEnd = True
        while isEnd:
            for player in range(1,self.players + 1):
                print("玩家"+ str(player) + "請輸入大於" + str(self.min_num) + "和小於" + str(self.max_num) + "的正整數")
                player_answer = int(input())
                if player_answer < self.final_num :
                    self.min_num = player_answer
                elif player_answer > self.final_num :
                    self.max_num = player_answer
                if self.final_num == player_answer :
                    print("玩家"+ str(player) + "猜中密碼")
                    isEnd = False
                    break

a = GuessGame(200, 1)
a.runguess()
        
    
        