
#adb万国挖宝石RedmiK40
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

def adb(index,gem):
    while (getKey() != 'lock'):
        time.sleep(1)
        if getKey() == 'down' or getKey() == 'other':
            os.system('adb shell input tap 600 50') #点击坐标
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input tap 1200 220')
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input text "'+str(gem[index][0])+'"') #输入横坐标
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input tap 2145 1000') #右下角打字确定键
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input tap 1430 220')
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input text "'+str(gem[index][1])+'"') #输入纵坐标
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input tap 2145 1000') #右下角打字确定键
            if getKey() == 'up':
                os.system('adb shell input tap 960 120')#退出坐标UI
                continue
            os.system('adb shell input tap 1575 220') #移动至该坐标
        if getKey() == 'up':
            time.sleep(2)
        index = index + 1
        if index == len(gem):
            index = 0

if __name__=="__main__":
    gem = [(815,723),(822,844),(843,691),(722,678),(941,722),(793,728),(820,726),(847,691),(790,690),(866,658),(777,663),(808,737),(854,734),(926,681),(772,769),(759,716),(710,621),(771,627),(874,766),(815,840)]
    index = 0
    while(1):
        time.sleep(3)
        if getKey() == 'downing':
            adb(index,gem)
