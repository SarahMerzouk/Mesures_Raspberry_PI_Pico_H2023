from machine import Pin, I2C
from I2C_LCD import I2cLcd
import time

def calculDistance():
    distance = 0
    try :
        velocite_son = 340

        trigger.value(1)
        time.sleep_us(10)
        trigger.value(0)
        
        while not echo.value():
            pass
        ping_debut = time.ticks_us()

        while echo.value():
            pass
        ping_fin = time.ticks_us()
        
        distance_temps = time.ticks_diff(ping_fin, ping_debut)
        distance = (velocite_son * distance_temps)
    except:
        pass
        
    return distance

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd_ecran = I2cLcd(i2c, I2C_ADDR, 2, 16)

# LED
led_rouge = Pin(16, Pin.OUT)
led_verte = Pin(9, Pin.OUT)

# CAPTEUR DE DISTANCE
trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)
distance = 0

led_rouge.on()
led_verte.on()

distance = calculDistance()
lcd_ecran.putstr(str(distance))
time.sleep(3)

lcd_ecran.clear()
nb = 3
rep = "ANGLE;" + str(nb)
reponses = rep.split(";")

lcd_ecran.putstr(str(reponses[1]))