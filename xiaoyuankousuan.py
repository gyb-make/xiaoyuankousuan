from PIL import ImageGrab
import pytesseract
import time
import keyboard
import ctypes
import os

#数字围成一个框把数字包起来就行
#左边数字的左上角
l_lup_x = 1751
l_lup_y = 449
#左边数字的右下角
l_rdown_x = 1873
l_rdown_y = 543
#右边数字的左上角
r_lup_x = 1991
r_lup_y = 445
#右边数字的右下角
r_rdown_x = 2112
r_rdown_y = 539

# tesseract.exe路径
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def get_box_num(x1, y1,x2, y2):
    img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    text = pytesseract.image_to_string(img, config="--psm 6")
    nums = []
    for s in text.split():
        if s.strip().isdigit():
            nums.append(int(s.strip()))
    return nums

# 从脚本所在目录找 mouse.dll，不依赖工作目录
dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mouse.dll")
mouse = ctypes.CDLL(dll_path)
mouse.MoveTo.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_double]
mouse.MouseDown.argtypes = []
mouse.MouseUp.argtypes = []

speed = 0.1

def xiaoyu():
    mouse.MouseUp()
    mouse.MoveTo(2145, 836, speed)
    mouse.MouseDown()
    mouse.MoveTo(1835, 1012, speed)
    mouse.MouseUp()
    mouse.MouseDown()
    mouse.MoveTo(2129, 1176, speed)
    mouse.MouseUp()

def dayu():
    mouse.MouseUp()
    mouse.MoveTo(1785, 850, speed)
    mouse.MouseDown()
    mouse.MoveTo(2068, 960, speed)
    mouse.MouseUp()
    mouse.MouseDown()
    mouse.MoveTo(1784, 1194, speed)
    mouse.MouseUp()

def is_valid_num(s):
    try:
        n = int(s.strip())
        return 1 <= n <= 20
    except (ValueError, TypeError):
        return False



right_resul = 0
left_result = 0

print("一秒后开始")
time.sleep(1)
print("开始")

'''
if __name__ == "__main__":
    while 1:
        if keyboard.is_pressed('space'):
            left_result = get_box_num(1751, 449,1873, 543)
            right_result = get_box_num(1991, 445,2112, 539)
            print("识别数字：", left_result,right_result)
            if left_result > right_result:
                dayu()
            elif left_result < right_result:
                xiaoyu()
            time.sleep(0.2) #防连按
        if keyboard.is_pressed('esc'):
            break
'''
if __name__ == "__main__":
    while 1:
        if  not keyboard.is_pressed('space'):
            if is_valid_num:
                left_result = get_box_num(l_lup_x, l_lup_y,l_rdown_x, l_rdown_y)
                right_result = get_box_num(r_lup_x, r_lup_y,r_rdown_x, r_rdown_y)
                print("识别数字：", left_result,right_result)
                if left_result > right_result:
                    dayu()
                elif left_result < right_result:
                    xiaoyu()
            time.sleep(0.5)
            
