# HC-SR501
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

push = 20
relay = 21

GPIO.setup(push, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)

print ("Start!!")
time.sleep(2)

try:
    while True:
        #if GPIO.input(push):
        print ("Waitig for sensor to settle")
        GPIO.wait_for_edge(push, GPIO.RISING, bouncetime=100)
        time.sleep(0.1)
        if GPIO.input(push)==1:
            print ("Motion Detected")
            GPIO.output(relay, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(relay, GPIO.LOW)
            print ("Detected")
            time.sleep(3)
        else:
            print ("miss..")
            time.sleep(1)
except:
    GPIO.cleanup()
    
        
      
      
