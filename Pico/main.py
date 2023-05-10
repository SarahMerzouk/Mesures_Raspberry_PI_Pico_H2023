from machine import Pin, I2C
import time
from I2C_LCD import I2cLcd
from random import randint
from myservo import Servo
import sys
from picozero import DistanceSensor
############################FONCTIONS##############################
def clignoterLumiere(ledChoisie) :
    i = 0
    while i < 3 :
        if ledChoisie == led_rouge:
            led_rouge.on()
            time.sleep_ms(1000)
            led_rouge.off()
            time.sleep_ms(1000)
        else:
            led_verte.on()
            time.sleep_ms(1000)
            led_verte.off()
            time.sleep_ms(1000)
        i+=1
###################################################################

# LED
led_rouge = Pin(16, Pin.OUT)
led_verte = Pin(9, Pin.OUT)

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd_ecran = I2cLcd(i2c, I2C_ADDR, 2, 16)

# CAPTEUR DE DISTANCE
ds = DistanceSensor(echo=18, trigger=19)

# SERVOMOTEUR
# rouge dans le VBUS à i1
# orange dans le GP2 à a4
# bleue dans le GND à a3
servo = Servo(2)
servo.ServoAngle(0)

###################### CAPTATION DE DONNÉES ######################
lcd_ecran.clear()
led_rouge.off()
led_verte.off()

try :
    while True:    
                
        rep = sys.stdin.readline().strip()
        servo.ServoAngle(0) 
        
        # si on mesure la distance
        if rep.lower() == "distance":

            distance = ds.distance
            
            # envoyer la distance à l'hôte
            print(distance)
            
            lcd_ecran.clear()
            lcd_ecran.move_to(0,0)
            lcd_ecran.putstr("Distance: ")
            lcd_ecran.move_to(0,1)
            lcd_ecran.putstr(str(distance) + " m")
            
            # faire clignoter la lumière verte quelques fois
            led_rouge.off()
            clignoterLumiere(led_verte)
            led_verte.on()
            
        elif rep.lower() == "angle":
            angle = randint(1,360)
            
            # envoyer l'angle à l'hôte
            print(angle)
            
            lcd_ecran.clear()
            lcd_ecran.move_to(0,0)
            lcd_ecran.putstr("Angle: ")
            lcd_ecran.move_to(0,1)
            lcd_ecran.putstr(str(angle) + " ")
            
            servo.ServoAngle(angle)
            
            # faire clignoter la lumière verte quelques fois
            led_rouge.off()
            clignoterLumiere(led_verte)
            led_verte.on()
        
        elif rep.lower() == "off":
            led_verte.off()
            clignoterLumiere(led_rouge)
        
            lcd_ecran.clear()
            lcd_ecran.move_to(0,0)
            lcd_ecran.putstr("Le systeme")
            lcd_ecran.move_to(0,1)
            lcd_ecran.putstr("est arretee!")
except:
    pass