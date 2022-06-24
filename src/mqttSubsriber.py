import paho.mqtt.client as mqtt
from queue import Queue

class Client:
    def __init__(self, topic):
        self.__topic = topic
        self.__client = mqtt.Client()
        self.__queue = Queue()
    
    def __on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.__client.subscribe(self.__topic)

    def __on_message(self, client, userdata, msg):
        print("Mqtt value: %s" %msg.payload)
        self.__queue.put(msg.payload.decode("utf-8"))
    
    def __eventMqtt(self):
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message

    def __createConnection(self):
        self.__eventMqtt()
        return self.__client.connect("broker.emqx.io", 1883, 60)

    def connect_loop_forever(self):
        self.__createConnection()
        return self.__client.loop_forever()

    def mqttValue(self):
        return self.__queue
