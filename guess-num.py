import random
x = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('请输入你猜的数字: ')
    num = float(num)
    if num == x:
        print('终于猜对了')
        print('这是你猜的第', count, '次')
        break
    elif num < x:
        print('比答案小')
    elif num > x:
        print('比答案大')
    print('这是你猜的第', count, '次')