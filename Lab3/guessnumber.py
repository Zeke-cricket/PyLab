## 輸入玩家人數
## 玩家猜數字猜到的遊戲結束
## 調整最大值 和 最小值
## initial game

import random

class GuessGame :
    def __init__ (self,player_num=2,max_num=100,min_num=1,isEnd = False,player_input=0):
        self.player_num = player_num
        self.answer = random.randint(min_num,max_num)
        self.isEnd = isEnd
        self.max_num = max_num
        self.min_num = min_num
        self.player_input = player_input
    def equal_ans(self,input_num):
        return self.answer == input_num
    def adjust_num(self,input_num):
        ## 邏輯性
        if (input_num > self.answer) and (input_num > self.min_num):
            self.max_num = input_num
        else:
            self.min_num = input_num

##player_input ##遺留程式碼 被利用性最低

## initial game
guessGame1 = GuessGame()
print(guessGame1.answer)


while not guessGame1.equal_ans(guessGame1.player_input) :
    guessGame1.player_input = int(input())
    if not guessGame1.equal_ans(guessGame1.player_input):
        guessGame1.adjust_num(guessGame1.player_input)
        print("Please input the number between " + str(guessGame1.max_num) + " And " + str(guessGame1.min_num))
    else:
        print("some one guess answer")
##"break"