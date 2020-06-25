######  NAME : Nikhil Gowda Shivaswamy
##      Matricualtion number: 11013382
## File Name: Main_Traffic.py

##Description: Embedded main project
## Designed for developing a traffic system
##I2C is confiqured 

##Board: Rasberry pi 3b

## I2C confiqured with: PCA9685

## IMPORTANT NOTE:All identifiers of variables are started with NG
## NG: Nikhil Gowda is an identical identifier which i used to write
#python software.

    # Main program starts from here for Two traffic lights
    # on the narrow line of river bridge


from board import  SCL , SDA
import busio
import time
from adafruit_pca9685 import PCA9685


  # FUNCTION DEFINITIONS FOR ALL 4 PHASES OF TRAFFIC SYSTEM
      # set RED is on
      #opposite side should move so Green LED is ON

      
def NG_phase_1():
    NG_pca9685.channels[NG_trafficLight_0].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_OPP_2].duty_cycle = NG_onLED
    print("Red Light is on - PLEASE STOP")
    print("line is now allowed and Green is ON")
    time.sleep(3)
    NG_pca9685.channels[NG_trafficLight_0 ].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_OPP_2].duty_cycle = NG_offLED
    return

       # set red and amber is on
      #opposite side should get ready to
       # -- to stop the vehicle so amber LED is ON

def NG_phase_2():
    NG_pca9685.channels[NG_trafficLight_0].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_1].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_OPP_1].duty_cycle = NG_onLED
    print("Red and amber Light is on - PLEASE STOP")
    print("line is now ready to stop and amber is ON")
    time.sleep(3)
    NG_pca9685.channels[NG_trafficLight_0].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_1].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_OPP_1].duty_cycle = NG_offLED
    return

      # set Green is on
      #opposite side should stop red LED is ON


def NG_phase_3():
    NG_pca9685.channels[NG_trafficLight_2].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_OPP_0].duty_cycle = NG_onLED
    print("Green Light is on - YOU CAN MOVE NOW")
    print(" line is on red - please stop ")
    time.sleep(3)
    NG_pca9685.channels[NG_trafficLight_2].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_OPP_0].duty_cycle = NG_offLED
    return

      # set amber is on
      #opposite side should break and stop amber and red LED is ON

def NG_phase_4():
    NG_pca9685.channels[NG_trafficLight_1].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_OPP_0].duty_cycle = NG_onLED
    NG_pca9685.channels[NG_trafficLight_OPP_1].duty_cycle = NG_onLED
    print("Amber Light is on")
    print("Amber and red Light is on")
    time.sleep(3)
    NG_pca9685.channels[NG_trafficLight_1].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_OPP_0].duty_cycle = NG_offLED
    NG_pca9685.channels[NG_trafficLight_OPP_1].duty_cycle = NG_offLED
    return

     # set the all LEDs off

def NG_allLEDsoff():
    for NG_trafficLightNr in range (10):
        NG_pca9685.channels[NG_trafficLightNr].duty_cycle = NG_offLED
    return


   # Creating the I2C bus interface from 'busio and board'.
   
NG_i2c_bus  = busio.I2C(SCL,SDA)

   # Creating a simple PCA9685 class instance.
   
NG_pca9685  = PCA9685(NG_i2c_bus)


#set frequency for pwm
NG_pca9685.frequency = 50  #hz

NG_onLED                = 65535  # PWM duty cycle 100%(full bright)
NG_offLED               =     0   # PWM duty cycle 0%(complete dim)
   ##Creating channels for all led
NG_trafficLight_0       =     0  # Red LED
NG_trafficLight_1       =     1  # AMBER LED
NG_trafficLight_2       =     2  #Green LED
NG_trafficLight_OPP_0   =     4  #Red LED at anoter side(opposite way)
NG_trafficLight_OPP_1   =     5  #Amber LED at anoter side(opposite way)
NG_trafficLight_OPP_2   =     6  #Green LED at anoter side(opposite way)



print ("Start")
NG_allLEDsoff()
print("To finish press ctrl c")
try:
    while True:
        
        print()
        
        ## calling function as per the requidred phases
        NG_phase_1()
        print()
        NG_phase_2()
        print()
        NG_phase_3()
        print()
        NG_phase_4()

except:
    NG_allLEDsoff()
    print("pressed ctrl c")
    print("finish")
    
