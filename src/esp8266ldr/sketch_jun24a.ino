#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi
const char *ssid = "sadamuhiz"; // Enter your WiFi name
const char *password = "sa2903dam";  // Enter WiFi password

// MQTT Broker
const char *mqtt_broker = "broker.emqx.io";
const char *topic = "raspberry/led";
const char *mqtt_username = "emqx";
const char *mqtt_password = "public";
const int mqtt_port = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(200);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");

  client.setServer(mqtt_broker, mqtt_port);
  while (!client.connected()) {
      String client_id = "esp8266-client-";
      client_id += String(WiFi.macAddress());
      Serial.printf("The client %s connects to the public mqtt broker\n", client_id.c_str());
      if (client.connect(client_id.c_str(), mqtt_username, mqtt_password)) {
          Serial.println("Public emqx mqtt broker connected");
      } else {
          Serial.print("failed with state ");
          Serial.print(client.state());
          delay(1000);
      }
  }
}

void loop() {
  client.loop();
  int ldrValue = analogRead(A0);
  if(ldrValue >= 750) {
    client.publish(topic, "ON");  
  } else {
    client.publish(topic, "OFF");  
  }
  delay(500);
}
