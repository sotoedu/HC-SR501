# HC-SR501
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) 

push = 26
relay = 21
sensor = 13

count = 0


GPIO.setup(push, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sensor, GPIO.IN)

print ("Start!!")
sleep(2)

print("This is my file to demonstrate best practices.")

def pushButton():
    #GPIO.wait_for_edge(push, GPIO.RISING, bouncetime=100)
    #sleep(0.1)
    global count
    
    if GPIO.input(push)==0:
            print ("Push Detected")
            GPIO.output(relay, GPIO.HIGH)
            sleep(3)
            GPIO.output(relay, GPIO.LOW)
            print ("Detected")
            sleep(3)
            count = 0
    else:
        print ("miss..")
        sleep(0.1)

def sensorPIR():
    global count
    if GPIO.input(sensor)==1:
        sleep(1)
        print ("Motion Detected: ", count)
        count += 1
    else:
        print ("Motion miss..")
        #sleep(0.5)
    
def main():
    result = 0
    
    try:
        sleep(2)
        while True:
            print("Waitig for sensor to settle ")
            sensorPIR()
            pushButton()
            sleep(0.3)
            
    except Exception as error:
        GPIO.cleanup()
        print ("except miss..", error)

if __name__ == "__main__":
    main()