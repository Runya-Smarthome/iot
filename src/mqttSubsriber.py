import paho.mqtt.client as paho
from paho import mqtt
from queue import Queue

class Client:
    def __init__(self, topic):
        self.__topic = topic
        self.__client = paho.Client(client_id="mqttx_807ce6bc", userdata=None, protocol=paho.MQTTv5)
        self.__queue = Queue()
    
    def __on_connect(self, client, userdata, flags, rc, properties=None):
        print(f"Connected with result code {rc}")
        self.__client.subscribe(self.__topic)

    def __on_message(self, client, userdata, msg):
        print("Mqtt value: %s" %msg.payload.decode("utf-8"))
        self.__queue.put(msg.payload.decode("utf-8"))
    
    def __eventMqtt(self):
        self.__client.on_connect = self.__on_connect
        self.__client.on_message = self.__on_message
        self.__client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        self.__client.username_pw_set("raspi", "raspiccit")

    def __createConnection(self):
        self.__eventMqtt()
        return self.__client.connect("80a2394d39414c4386f58ac618f6ae44.s2.eu.hivemq.cloud", 8883)

    def connect_loop_forever(self):
        self.__createConnection()
        return self.__client.loop_start()

    def mqttValue(self):
        return self.__queue

