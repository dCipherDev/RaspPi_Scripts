import os
import time, datetime 
from time import sleep
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
        
sense = SenseHat()
sense.set_rotation(180)
sense.set_imu_config(False, False, False)
sense.low_light = True

s=(0.065) # scroll speed
w=(0) # color all white toggle
x=(2) #shutdown variable

# is really stick down
def pushed_up(event):
    if event.action == ACTION_PRESSED:
       sense.low_light = True
        
# is really stick up
def pushed_down(event):
    if event.action == ACTION_PRESSED:
       sense.low_light = False

#is really stick right
def pushed_left(event):
    global w
    if event.action == ACTION_PRESSED:
        w = (255)
        
# is really stick left
def pushed_right(event):
    global w
    if event.action == ACTION_PRESSED:
        w = (0)

def pushed_middle(event):
    global x
    if event.action == ACTION_PRESSED:
        x = 0

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle

while True:

    dateString = "%A %B %-d %-I:%M %p"
 #   msg = "It is %s" % (datetime.datetime.now().strftime(dateString))
 #   sense.show_message(msg, scroll_speed=s, text_colour=(w, 255, 255))

    t = sense.get_temperature()
    t = round(t)
          
    if t <= 0: 
        tc = [w, w, 255]  # blue
    elif t > 0 and t < 20:
        tc = [255, 255, w]  # yellow
    elif t >= 20 and t <= 35:
        tc = [w, 255, w]  # green
    elif t > 35:
        tc = [255, w, w]  # red                 
    msg = " %sc" % (t)
    sense.show_message(msg, scroll_speed=s, text_colour=tc)
    sense.clear()
    sleep(5)
"""
    h = sense.get_humidity()
    h = round(h)
    if h > 100:
       h = 100

    if h >= 30 and h <= 60:
        hc = [w, 255, w]  # green
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)
    elif h > 60 and h < 80:
        hc = [255, 255, w]  # yellow
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)
    else:
        hc = [255, w, w]  # red
        msg = "with %s%% Humidity" % (h)
        sense.show_message(msg, scroll_speed=s, text_colour=hc)

    p = sense.get_pressure()
    p = round(p)
        
    if p >= 960 and p < 985:
        pc = [255, w, w]  # red
        msg = "- Barometer is Very Low @ %smb - Storm Watch" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 985 and p < 1005:
        pc = [255, 255, w]  # yellow
        msg = "- Barometer is Low @ %smb - Possible Percipitationb" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1005 and p < 1025:
        pc = [w, 255, w]  # green
        msg = "- Barometer is Mid Range @ %smb" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1025 and p < 1050:
        pc = [w, w, 255]  # blue
        msg = "- Barometer is High @ %smb" % (p)
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
    elif p >= 1050:
        pc = [255, w, w]  # red
        msg = "- Barometer is Very High @ %smb - Expect Dry Conditions" % (p) 
        sense.show_message(msg, scroll_speed=s, text_colour=pc)
        
    if x == 0:
        os.system("sudo shutdown now -P")
    elif x == 1:
        raise SystemExit
"""
# Last edited on March 14th 2018
# run sudo crontab -e
# add
# @reboot python3 /home/pi/THP.py &



