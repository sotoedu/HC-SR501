# HC-SR501
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

# laser(KY008) = VCC 5.5, GND, GPIO17 
# cds = VCC 3.3, GND, GPIO18

laser = 17
light = 18

count = 0


GPIO.setup(light, GPIO.IN)
GPIO.setup(laser, GPIO.OUT)

print ("Start!!")
GPIO.output(laser, GPIO.LOW)
sleep(2)
GPIO.output(laser, GPIO.HIGH)

print("This is my file to demonstrate best practices.")

def sensorPIR():
    global count
    
    data = GPIO.input(light)
    sleep(0.005)
    print ("Motion Detected0: ", data)
    
def main():
    result = 0
    
    try:
        sleep(2)
        while True:
            print("Waitig for sensor to settle ")
            sensorPIR()
            sleep(0.2)
            
    except Exception as error:
        GPIO.cleanup()
        print ("except miss..", error)

if __name__ == "__main__":
    main()