#請做出一支能猜數字的程式：每次讓使用者猜一個整數，若猜對就輸出Bingo；使用者最多可以猜3次。(提示: Bingo後可以使用break來離開迴圈)

a = int(input("Guess a number? (1-10) "))
times = 1

import random
c_choice = random.randint(1,10)

for i in range(3):
  if a == c_choice:
    print("Bingo")
    break

  elif times == 3:
    print("Game Over!")
  
  elif a > c_choice:
    a = int(input("The answer is smaller. Try again~ "))
    times += 1

  elif a < c_choice:
    a = int(input("The answer is bigger. Try again~ "))
    times += 1

    
#for loop exercise from https://kopu.chat/2017/01/18/一小時python入門-part-1/
