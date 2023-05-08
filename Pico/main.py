from machine import Pin, I2C
import time
from I2C_LCD import I2cLcd
#from myservo import Servo
import sys
############################FONCTIONS##############################
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

def calculAngle(valeur):
    angle = (valeur * 180) / 65535
    
    return int(angle)

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
trigger = Pin(19, Pin.OUT)
echo = Pin(18, Pin.IN)
distance = 0

# SERVOMOTEUR
# rouge dans le VBUS à i1
# orange dans le GP2 à a4
# bleue dans le GND à a3

#servo = Servo(2)
#servo.ServoAngle(0)

###################### CAPTATION DE DONNÉES ######################
lcd_ecran.clear()
led_rouge.off()
led_verte.off()

try :
    while True:    
                
        rep = sys.stdin.readline().strip() 
        
        # si on mesure la distance
        if rep.lower() == "distance":

            distance = calculDistance()
            
            lcd_ecran.clear()
            lcd_ecran.move_to(0,0)
            lcd_ecran.putstr("Distance: ")
            lcd_ecran.move_to(0,1)
            lcd_ecran.putstr(str(distance) + " cm")
            
            # envoyer la distance à l'hôte
            print(distance)
            
            # faire clignoter la lumière verte quelques fois
            led_rouge.off()
            clignoterLumiere(led_verte)
            led_verte.on()
except:
    pass