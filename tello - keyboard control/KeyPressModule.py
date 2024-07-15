
# project: use keyboard to control drone
# control keys: 
# e - take off
# q - land
# w,s,a,d - control key
# arrow - control key

from djitellopy import tello
import keyboard as kb
from time import sleep
import cv2

kb.init()
me = tello.Tello()
me.connect()
me.streamon()
print("battery status: ", me.get_battery())

def getKeyBoardInput():
    lr,fb,ud,yv = 0, 0, 0, 0
    speed = 100

    if kb.getKey("LEFT"): lr = -speed
    elif kb.getKey("RIGHT"): lr = speed

    if kb.getKey("UP"): fb = speed
    elif kb.getKey("DOWN"): fb = -speed

    if kb.getKey("w"): ud = speed
    elif kb.getKey("s"): ud = -speed

    if kb.getKey("a"): yv = -speed
    elif kb.getKey("d"): yv = speed

    if kb.getKey("q"): me.land()
    if kb.getKey("e"): me.takeoff()

    return [lr,fb,ud,yv]

while True:
    vals = getKeyBoardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
