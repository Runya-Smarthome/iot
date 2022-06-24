import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

class Lamp:
    def __init__(self):
        pass

    @staticmethod
    def firstLamp(queue):
        queueMessage = ""
        while True:
            while not queue.empty():
                queueMessage = str(queue.get())
                if(queueMessage == "ON") :
                    GPIO.output(8, GPIO.HIGH)
                elif(queueMessage == "OFF"):
                    GPIO.output(8, GPIO.LOW)