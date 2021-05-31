# HC-SR501
import RPi.GPIO as GPIO
import time
from playsound import playsound
import os

file = "./final.mp3"


while True:
    print("startgo response")
    playsound("startgo.mp3")
    print("final response")
    time.sleep(2)
    playsound("final.mp3")
    time.sleep(2)
    print("final response")
    
    os.system( 'mpg321 ' + file)
    time.sleep(3)

