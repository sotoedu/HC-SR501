# HC-SR501

Relay
GPIO21 --  relay signal
2      --  relay VCC
6      --  relay GND

Push Button
GPIO20 --  Push RED(+)
39     --  Push BLACK(-)
 

HC-SR501 움직임센서

    import RPi.GPIO as GPIO
    import time
    GPIO.setmode(GPIO.BCM) 

    sensor = 23
    led = 22

    GPIO.setup(sensor, GPIO.IN)
    GPIO.setup(led, GPIO.OUT)

    print "Waitig for sensor to settle"
    time.sleep(2)
    print "Detecting motion"

    while True:
      if GPIO.input(sensor):
        print "Motion Detected"
        GPIO.output(led, True)
        time.sleep(2)
      GPIO.output(led, False)
      time.sleep(2)
