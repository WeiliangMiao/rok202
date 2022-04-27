#!/usr/bin/env python3
#adb万国打野人脚本RedmiK40
import os
import time

def getKey():
    key = os.popen('adb shell dumpsys window policy|grep mKeyPressed').read()
    if key == '      mKeyPressed=10000000 mKeyPressing=0 mShortcutPressing=0\n':
        return 'up'
    if key == '      mKeyPressed=1000000 mKeyPressing=0 mShortcutPressing=0\n':
        return 'down'
    if key == '      mKeyPressed=100000 mKeyPressing=0 mShortcutPressing=0\n':
        return 'lock'
    if key == '      mKeyPressed=1000000 mKeyPressing=1000000 mShortcutPressing=0\n':
        return 'downing'
    return 'other'

def adb():
    while (getKey() != 'lock'):
        time.sleep(1)
        if getKey() == 'down' or getKey() == 'other':
            os.system('adb shell input tap 160 800') #点击搜索
            os.system('adb shell input tap 625 945') #点击野蛮人
            os.system('adb shell input tap 660 730') #点击野蛮人搜索
            time.sleep(0.5)
            os.system('adb shell input tap 1200 540') #点击屏幕中间的野蛮人
            os.system('adb shell input tap 1633 720') #点击攻击野蛮人（位置在右侧）
            os.system('adb shell input tap 2180 1020') #点击多选
            os.system('adb shell input tap 2000 1000') #点击开始
            os.system('adb shell input tap 160 55') #点击头像
            os.system('adb shell input tap 930 615') #点击+号
            os.system('adb shell input tap 1716 389') #点击第一行使用
            os.system('adb shell input tap 1450 387') #点击x多个
            os.system('adb shell input tap 1890 121') #点击关闭
            os.system('adb shell input tap 1890 121') #点击关闭
            for _ in range(300):
                time.sleep(1)
                if getKey() == 'up':
                    os.system('adb shell input tap 960 120')#退出坐标UI
                    break
            
            
        if getKey() == 'up':
            time.sleep(2)


if __name__=="__main__":
    index = 0
    while(1):
        time.sleep(3)
        if getKey() == 'downing':
            adb()