import random
x = random.randint(1, 100)
while True:
    num = input('请输入你猜的数字: ')
    num = float(num)
    if num == x:
        print('终于猜对了')
        break
    elif num < x:
        print('比答案小')
    elif num > x:
        print('比答案大')