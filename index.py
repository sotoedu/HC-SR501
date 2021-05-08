# HC-SR501
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

push = 4
relay = 2

GPIO.setup(push, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

print "Waitig for sensor to settle"
time.sleep(2)
print "Detecting motion"

while True:
  if GPIO.input(push):
    print "Motion Detected"
    GPIO.output(relay, True)
    time.sleep(2)
    GPIO.output(realy, False)
    time.sleep(2)
