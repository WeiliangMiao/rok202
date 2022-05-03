#adb_rok_scan
#Redmi6 测试版，需要先手动进入界面
import time
import os
import random

def click(x,y,r):
    axes_x=x+random.randint(-r,r)
    axes_y=y+random.randint(-r,r)
    os.system('adb shell input tap '+str(axes_x)+' '+str(axes_y))
    time.sleep(0.2)
    return

os.system('adb devices')
os.system('adb shell am startservice ca.zgrs.clipper/.ClipboardService')

time.sleep(10)
click(401,225,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=os.popen('adb shell am broadcast -a clipper.get').read()[92:-2]
click(1171,83,1)    #点关闭

click(407,307,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=player_name+'\n'+os.popen('adb shell am broadcast -a clipper.get').read()[92:-2]
click(1171,83,1)    #点关闭

click(416,393,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=player_name+'\n'+os.popen('adb shell am broadcast -a clipper.get').read()[92:-2]
click(1171,83,1)    #点关闭

last_name=[]
for _ in range(300):
    click(415,476,5)
    x=[740,695,760,675,780]
    for __ in range(5):
        click(x[__],230,2)    #点。。。 
        click(x[__],157,4)    #点复制昵称
        click(900,200,5)
        name=os.popen('adb shell am broadcast -a clipper.get').read()[92:-2]
        if name==last_name:
            continue
        else:
            last_name=name
            player_name=player_name+'\n'+last_name
            break
    click(1171,83,1)    #点关闭

f = open('player_name.txt', "w", encoding="utf-8")
f.write(player_name)
f.close()