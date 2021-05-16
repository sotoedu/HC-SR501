# HC-SR501
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) 

push = 20
relay = 21
sensor = 16

count = 0


GPIO.setup(push, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(relay, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sensor, GPIO.IN)

print ("Start!!")
sleep(2)

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def sensorPIR():
    global count
    if GPIO.input(sensor)==1:
        sleep(0.5)
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
            sleep(1)
            
    except Exception as error:
        GPIO.cleanup()
        print ("except miss..", error)

if __name__ == "__main__":
    main()