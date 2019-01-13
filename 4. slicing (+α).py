#來辦場Party吧! 輸入十個整數、存入一個名為people清單中 (表示我們的宴客人數)；之後會有五次詢問，每次會輸入清單開始和結束的位置，再輸出從開始到結束位置的總和。
#last exercise from https://kopu.chat/2017/01/18/一小時python入門-part-1/ 


##input 10 numbers randomly and creat a list
print("Plz input ten numbers (1-10)")
people = []

for i in range(1, 11):
  while True: 
    try:
      people.append(int(input(str(i) + ": ")))
      break
    except ValueError:
      print("invalid input")
print(people)

##define slicing indexes and creat another list (var a should not be 9 or greater, may add a try/except to refine)
#code reference: https://stackoverflow.com/questions/41645898/using-a-loop-to-create-and-assign-multiple-variables-python
sum_list = []
def slice():
  for num in range(5):
    a = int(input("begin?(0-8) "))
    b = int(input("end?(1-9) "))

    if b <= a:
      print("end should be greater than start")
      b = int(input("end?(0-9) "))
    
    sum_list.append(a)
    sum_list.append(b)
  return sum_list

##sum up each slice and print out total (may refine the code with another function with loop later)
#code reference: https://stackoverflow.com/questions/14051916/python-how-to-make-a-local-variable-inside-a-function-global
lists = slice()
num1 = sum(people[lists[0]:lists[1]])
num2 = sum(people[lists[2]:lists[3]])
num3 = sum(people[lists[4]:lists[5]])
num4 = sum(people[lists[6]:lists[7]])
num5 = sum(people[lists[8]:lists[9]])

print(num1+num2+num3+num4+num5)
