from RPLCD.i2c import CharLCD
import threading
import RPi.GPIO as GPIO
import time
lcd = CharLCD("PCF8574",0x27)
Digit = [(),(),(),(),(),(),(),(),()]
#0的左上
Digit[0] = (
    0x07,
    0x0F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F
)
#0的右上
Digit[1] = (
    0x1C,
    0x1E,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F
)
#0的左下
Digit[2] = (
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x0F,
    0x07
)
#0的右下
Digit[3] = (
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1F,
    0x1E,
    0x1C
)
#0的正下
Digit[4] = (
    0x00,
    0x00,
    0x00,
    0x00,
    0x00,
    0x1F,
    0x1F,
    0x1F
)
#0的正上
Digit[5] = (
    0x1F,
    0x1F,
    0x1F,
    0x00,
    0x00,
    0x00,
    0x00,
    0x00
)
#8的上半
Digit[6] = (
    0x1F,
    0x1F,
    0x1F,
    0x00,
    0x00,
    0x00,
    0x1F,
    0x1F
)
for i in range(0,7):
    lcd.create_char(i,Digit[i])
def print_digit(number,pos):
    if number == 0:
        lcd.cursor_pos= (0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x05")
        lcd.write_string("\x01")
        lcd.cursor_pos = (1,pos)
        lcd.write_string("\x02")
        lcd.write_string("\x04")
        lcd.write_string("\x03")
    elif number == 1:
        lcd.cursor_pos=(0,pos+2)
        lcd.write_string("\x01")
        lcd.cursor_pos=(1,pos+2)
        lcd.write_string("\x03")
    elif number == 2:
        lcd.cursor_pos=(0,pos)
        lcd.write_string("\x06")
        lcd.write_string("\x06")
        lcd.write_string("\x01")
        lcd.cursor_pos=(1,pos)
        lcd.write_string("\x02")
        lcd.write_string("\x04")
        lcd.write_string("\x04")
    elif number == 3:
        lcd.cursor_pos=(0,pos)
        lcd.write_string("\x06")
        lcd.write_string("\x06")
        lcd.write_string("\x01")
        lcd.cursor_pos=(1,pos)
        lcd.write_string("\x04")
        lcd.write_string("\x04")
        lcd.write_string("\x03")
    elif number == 4:
        lcd.cursor_pos=(0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x04")
        lcd.write_string("\x01")
        lcd.cursor_pos=(1,pos+2)
        lcd.write_string("\x03")
    elif number == 5:
        lcd.cursor_pos=(0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x06")
        lcd.write_string("\x06")
        lcd.cursor_pos=(1,pos)
        lcd.write_string("\x04")
        lcd.write_string("\x04")
        lcd.write_string("\x03")
    elif number == 6:
        lcd.cursor_pos = (0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x06")
        lcd.write_string("\x06")
        lcd.cursor_pos = (1,pos)
        lcd.write_string("\x02")
        lcd.write_string("\x04")
        lcd.write_string("\x03")
    elif number == 7:
        lcd.cursor_pos = (0,pos)
        lcd.write_string("\x05")
        lcd.write_string("\x05")
        lcd.write_string("\x01")
        lcd.cursor_pos = (1,pos+2)
        lcd.write_string("\x03")
    elif number == 8:
        lcd.cursor_pos= (0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x06")
        lcd.write_string("\x01")
        lcd.cursor_pos = (1,pos)
        lcd.write_string("\x02")
        lcd.write_string("\x04")
        lcd.write_string("\x03")
    elif number == 9:
        lcd.cursor_pos= (0,pos)
        lcd.write_string("\x00")
        lcd.write_string("\x06")
        lcd.write_string("\x01")
        lcd.cursor_pos = (1,pos)
        lcd.write_string("\x04")
        lcd.write_string("\x04")
        lcd.write_string("\x03")

def timer_interruput():
    global second_cnt,flag
    flag = True
    timer = threading.Timer(1,timer_interruput)
    timer.start()
timer_interruput()
try:
    while True:
        if flag:
            flag = False
            t = time.localtime()
            if t.tm_sec == 0:
                lcd.clear()
            print_digit(t.tm_hour//10,0)
            print_digit(t.tm_hour%10,3)
            print_digit(t.tm_min//10,7)
            print_digit(t.tm_min%10,10)
            lcd.cursor_pos = (1,14)
            lcd.write_string(str(t.tm_sec//10)+str(t.tm_sec%10))
except KeyboardInterrupt:
    lcd.clear()
    lcd.cursor_pos = (1,3)
    lcd.write_string(" THE END ")
            