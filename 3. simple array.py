"""五次數學段考的成績分別為10、30、50、70、90分，算出平均後，老師發現大家考太爛、只好將成績開根號再乘上10 (提示: 成績**0.5*10)，再算出一個新平均。
請印出: 1. 五次成績; 2. 平均成績; 3. 五次新成績; 4. 新分數的平均。"""

import numpy as np

a = np.array([10, 30, 50, 70, 90])

print(a)
print(np.mean(a))
print(a**0.5*10)
print(np.mean(a**0.5*10))


#(list) exercise from https://kopu.chat/2017/01/18/一小時python入門-part-1/
#偷步用了array :p
