#adb_rok_scan
#Redmi6 测试版，需要先手动进入界面
import time
import pyperclip
import os
import random

def click(x,y,r):
    axes_x=x+random.randint(-r,r)
    axes_y=y+random.randint(-r,r)
    os.system('adb shell input tap '+str(axes_x)+' '+str(axes_y))
    return

time.sleep(10)
click(401,225,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=pyperclip.paste()
click(1171,83,1)    #点关闭

click(407,307,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=player_name+'\n'+pyperclip.paste()
click(1171,83,1)    #点关闭

click(416,393,5)
click(745,230,2)    #点。。。
click(744,157,4)    #点复制昵称
player_name=player_name+'\n'+pyperclip.paste()
click(1171,83,1)    #点关闭

for _ in range(10):
    click(415,476,5)
    click(745,230,2)    #点。。。
    click(744,157,4)    #点复制昵称
    player_name=player_name+'\n'+pyperclip.paste()
    click(1171,83,1)    #点关闭

f = open('player_name.txt', "w", encoding="utf-8")
f.write(player_name)
f.close()