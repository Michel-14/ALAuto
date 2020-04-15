import cv2
from util.adb import Adb
from PIL import Image

# A short script to take screen captures to contribute to the 720p bot version
# Works with Memu by default, refer to update_screen in utils.py to make it work with Bluestacks
# The output should be a 1080p upscaled version of the 720p screenshot

Adb.service = '192.168.0.17:5555'
Adb.tcp = False 
adb = Adb()
adb.exec_out('/storage/emulated/legacy/Download/ascreencap -f /storage/emulated/legacy/Download/screenshot.bmp')

screen = cv2.resize(cv2.imread("C:\\Users\\Michel14\\Downloads\\MEmu Download\\screenshot.bmp", 1),(1920,1080))

cv2.imwrite('screenshot.png', screen)