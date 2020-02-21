import time,os,random,datetime
a=0
while True:
    print('正在加载反黑程序……\n'+str(a)+'%')
    a+=1
    time.sleep(0.025)
    os.system('cls')
    if a==101:
        break
b=input('请输入要监视的电脑名称：')
print('输入Ctrl+C结束===开始监视，当前时间：',datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))
if b=='PC-14588594250':
    d=random.randint(1500,5000)
    while True:
        try:
            time.sleep(int(d))
            print(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'),'发现一次异常：试图攻击某人的IP地址以及计算机。')
        except KeyboardInterrupt:
            break
else:
    print('找不到计算机',b)
    time.sleep(5)
