#!/usr/bin/env python3
#adb万国八方开图
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
            os.system('adb shell input tap 164 978') #点击城市布局
            time.sleep(2)
            os.system('adb shell input tap 1119 644') #点击斥候营地
            os.system('adb shell input tap 1231 865') #点击进入斥候营地
            os.system('adb shell input tap 1735 477') #点击第一个斥候
            time.sleep(2)
            os.system('adb shell input tap 1447 728') #点击地图探索
            os.system('adb shell input tap 1942 251') #点击第一个斥候出发

            os.system('adb shell input tap 164 978') #点击城市布局
            time.sleep(2)
            os.system('adb shell input tap 1119 644') #点击斥候营地
            os.system('adb shell input tap 1231 865') #点击进入斥候营地
            os.system('adb shell input tap 1754 670') #点击第二个斥候
            time.sleep(2)
            os.system('adb shell input tap 1447 728') #点击地图探索
            os.system('adb shell input tap 1920 442') #点击第二个斥候出发

            os.system('adb shell input tap 164 978') #点击城市布局
            time.sleep(2)
            os.system('adb shell input tap 1119 644') #点击斥候营地
            os.system('adb shell input tap 1231 865') #点击进入斥候营地
            os.system('adb shell input tap 1750 865') #点击第三个斥候
            time.sleep(2)
            os.system('adb shell input tap 1447 728') #点击地图探索
            os.system('adb shell input tap 1949 636') #点击第三个斥候出发
            time.sleep(2)
            
            for _ in range(80):
                time.sleep(1)
                if getKey() == 'up':
                    #os.system('adb shell input tap 960 120')#退出坐标UI
                    break
            
            
        if getKey() == 'up':
            time.sleep(2)


if __name__=="__main__":
    index = 0
    while(1):
        time.sleep(10)
        if getKey() == 'downing':
            adb()