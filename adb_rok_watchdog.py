#adb_rok_watchdog
#Redmi6 1440*720 >=kvk4
import os
import time
import random
from PIL import Image
import pyperclip

def click(x,y,r):
    axes_x=x+random.randint(-r,r)
    axes_y=y+random.randint(-r,r)
    os.system('adb shell input tap '+str(axes_x)+' '+str(axes_y))
    return

while 1:
    player_name = []
    for line in open("player_name.txt"):
        player_name = player_name + line
    time.sleep(15)
    click() #防掉线
    time.sleep(10)
    click(1192,669,10)  #点联盟
    time.sleep(1)
    click(1142,554,15)  #点设置
    time.sleep(1)
    click(421,462,15)   #点审核
    time.sleep(1)
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png ./')
    img1 = Image.open('screenshot.png')
    img1 = img1.crop((1103,229,1188,277))
    img2 = Image.open('save_crop.png')
    if img1.convert('1')==img2.convert('1'):
        click(276,254,5)    #点申请人头像
        click(745,230,2)    #点。。。
        click(744,157,4)    #点复制昵称
        click(997,141,30)   #点开
        click(1171,83,1)    #点关闭
        if pyperclip.paste() in player_name:
            click(1150,250,5)   #点勾
            

    else:
        break
