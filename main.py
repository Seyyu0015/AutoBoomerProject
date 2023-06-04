import time

import pydirectinput
import win32api
import win32con
import win32gui
import pyautogui

test = True
in_fight = False

# 俯冲
dive_range = 2  # 俯冲移动鼠标次数 默认
dive_coefficient = 20  # 俯冲移动鼠标幅度 默认
dive_time = 20  # 俯冲保持时间 默认

state = "车库"


# 战雷位置
# title = "War Thunder"
# window = win32gui.FindWindow(None, title)
# pos = win32gui.GetWindowRect(window)
# window_rect = (pos[0], pos[1], pos[2] - pos[0], pos[3] - pos[1])
# print("窗口位置", window_rect)


def join():
    global state
    print('')
    print("- 当前状态 > ", state, end='')
    if state == "车库":
        print('')
        print("- 准备开始匹配 > ", end='')
        rect = pyautogui.locateOnScreen('img/fight.png', confidence=0.7)
        if rect is not None:
            print("按下开始按键", end='')
            pyautogui.moveTo(rect)
            state = "出生"
            rect = None

    if state == "出生":
        print('')
        print("- 准备出飞机 > ", end='')
        rect = pyautogui.locateOnScreen('img/join.png', confidence=0.7)
        if rect is not None:
            print("按下出生按键", end='')
            pyautogui.moveTo(rect)
            state = "俯冲"
            rect = None

    if state == "俯冲":
        print('')
        print("- 准备俯冲 > ", end='')
        rect = pyautogui.locateOnScreen('img/pointer.png', confidence=0.6)
        if rect is not None:
            time.sleep(3)
            for i in range(3):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -60, 0)
                time.sleep(0.2)
            time.sleep(3)
            print("开始俯冲...", end='')
            for i in range(dive_range):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, dive_coefficient)
                time.sleep(0.2)
            time.sleep(dive_time)
            print("开始拉平...", end='')
            for i in range(dive_range):
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, -dive_coefficient)
                time.sleep(0.2)
            print("俯冲结束", end='')
            state = "赶路"
            rect = None


def restart():
    global state
    print('')
    print("- 是否已经结束 > ", end='')
    if pyautogui.locateOnScreen('img/return.png', confidence=0.8) is not None:
        print("退出游戏 > ", end='')
        rect = pyautogui.locateOnScreen('img/return.png', confidence=0.8)
        pyautogui.moveTo(rect)
        rect = None

    if pyautogui.locateOnScreen('img/restart.png', confidence=0.8) is not None:
        print("返回基地", end='')
        rect = pyautogui.locateOnScreen('img/restart.png', confidence=0.8)
        pyautogui.moveTo(rect)
        time.sleep(2)
        state = "车库"


def watch_base():
    print('')
    print("- 寻找战区 > ", end='')
    if pyautogui.locateOnScreen('img/base.png', confidence=0.5) is not None:
        print("战区位置 > ", pyautogui.locateOnScreen('img/base.png', confidence=0.6), end='')
        print('')
        print("- 准星位置 > ", pyautogui.locateOnScreen('img/pointer.png', confidence=0.6), end='')


while True:
    print("")
    print("————————————————", end='')
    #
    # join()
    # restart()
    watch_base()

    time.sleep(3)
