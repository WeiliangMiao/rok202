#adb_rok_watchdog
#Redmi6 1440*720 >=kvk4
import os
import time
import random
from PIL import Image

def click(x,y,r):
    axes_x=x+random.randint(-r,r)
    axes_y=y+random.randint(-r,r)
    os.system('adb shell input tap '+str(axes_x)+' '+str(axes_y))
    time.sleep(1)
    return

os.system('adb devices')
os.system('adb shell am startservice ca.zgrs.clipper/.ClipboardService')
while 1:
    player_name = []
    for line in open("player_name.txt"):
        player_name = player_name + [line.replace('\n','')]
    time.sleep(15)
    click(721.476,10) #防掉线
    time.sleep(10)
    click(1192,669,10)  #点联盟
    click(1142,554,15)  #点设置
    click(421,462,15)   #点审核
    img2 = Image.open('save_crop.png')
    while(1):
        os.system('adb shell screencap -p /sdcard/screenshot.png')
        os.system('adb pull /sdcard/screenshot.png ./')
        img1 = Image.open('screenshot.png')
        img1 = img1.crop((1103,229,1188,277))
        time.sleep(2)
        if img1.convert('1')==img2.convert('1'):
            click(276,254,5)    #点申请人头像
            click(745,230,2)    #点。。。
            click(744,157,4)    #点复制昵称
            click(997,141,30)   #点开
            click(1171,83,1)    #点关闭
            if os.popen('adb shell am broadcast -a clipper.get').read()[92:-2] in player_name:
                click(1150,250,5)   #点勾
                os.system('adb shell am broadcast -a clipper.set -e text "这绝对不可能是昵称"')
            elif os.popen('adb shell am broadcast -a clipper.get').read()[92:-2]=="这绝对不可能是昵称":
                pass
            else:
                click(1042,250,5)   #点叉
        else:
            break
    
    click(1171,83,1)    #点关闭
    click(1171,83,1)    #点关闭
    click(1171,83,1)    #点关闭
