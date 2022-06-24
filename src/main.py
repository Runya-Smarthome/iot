from lamp import Lamp
from mqttSubsriber import Client
from threading import Thread

lamp = Lamp()
client = Client("raspberry/led")

if __name__ == "__main__":
    t1 = Thread(target=lamp.firstLamp, args=(client.mqttValue(),))
    t2 = Thread(target=client.connect_loop_forever)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass