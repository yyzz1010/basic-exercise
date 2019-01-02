#現在有一個 list a = [1, 3, 5, 7, 9]，請對每一個元素都平方後印出來，且須將 a 也變成 [1, 9, 25, 49, 81]。

a = [1, 3, 5, 7, 9]

for num in a:
  num = num**2
  print(num)

a = [num**2 for num in a]
print(a)


#lst = [y+z for y in [0,8] for z in [0,1,2,3]]
#trick from
#https://stackoverflow.com/questions/39322625/how-to-put-python-loop-output-in-a-list


#list exercise from https://kopu.chat/2017/01/18/一小時python入門-part-1/
