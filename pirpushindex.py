# HC-SR501
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) 

push = 20
relay = 21
sensor = 16

count = 0

GPIO.setup(push, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sensor, GPIO.IN)

print ("Start!!")
time.sleep(2)

def pushButton():
    GPIO.wait_for_edge(push, GPIO.RISING, bouncetime=100)
    time.sleep(0.1)
    
    if GPIO.input(push)==1:
            print ("Push Detected")
            GPIO.output(relay, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(relay, GPIO.LOW)
            print ("Detected")
            time.sleep(3)
            count = 0
    else:
        print ("miss..")
        time.sleep(1)
    
def sensorPIR(count):
    if GPIO.input(sensor)==1:
            print ("Motion Detected")
            GPIO.output(relay, GPIO.HIGH)
            time.sleep(3)
            count += 1
    else:
        print ("Motion miss..")
        time.sleep(1)
    
    return count

def main():
    try:
        while True:
            print("Waitig for sensor to settle: ", count)
            count = sensorPIR(count)
            
    except:
        GPIO.cleanup()
        print ("except miss..")
            

if __name__ == "__main__":
    main()
    
