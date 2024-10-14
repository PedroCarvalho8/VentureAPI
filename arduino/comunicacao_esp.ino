#include <WiFi.h>
#include <HTTPClient.h>
#include <ESPAsyncWebServer.h>
#include <ArduinoJson.h>


int pin1_1 = 13;
int pin1_2 = 12;
int pin1_3 = 14;
int pin1_4 = 27;

int pin2_1 = 26;
int pin2_2 = 25;
int pin2_3 = 33;
int pin2_4 = 32;

const char* ssid = "Venture";
const char* password = "123456789";

AsyncWebServer server(80);

void alternar_frente(){
  digitalWrite(pin1_1, !digitalRead(pin1_1));
  digitalWrite(pin1_3, !digitalRead(pin1_3));
  digitalWrite(pin2_1, !digitalRead(pin2_1));
  digitalWrite(pin2_3, !digitalRead(pin2_3));
}

void alternar_tras(){
  digitalWrite(pin1_2, !digitalRead(pin1_2));
  digitalWrite(pin1_4, !digitalRead(pin1_4));
  digitalWrite(pin2_2, !digitalRead(pin2_2));
  digitalWrite(pin2_4, !digitalRead(pin2_4));
}

void setup() {
  pinMode(pin1_1, OUTPUT);
  pinMode(pin1_2, OUTPUT);
  pinMode(pin1_3, OUTPUT);
  pinMode(pin1_4, OUTPUT);

  pinMode(pin2_1, OUTPUT);
  pinMode(pin2_2, OUTPUT);
  pinMode(pin2_3, OUTPUT);
  pinMode(pin2_4, OUTPUT);

  Serial.begin(115200);
  WiFi.mode(WIFI_MODE_AP);
  WiFi.softAP(ssid, password);

  server.on("/frente", HTTP_GET, [](AsyncWebServerRequest * request) {
    alternar_frente();
    request->send(200, "text/plain", "Alternar andando para frente.");
  });

  server.on("/tras", HTTP_GET, [](AsyncWebServerRequest * request) {
    alternar_tras();
    request->send(200, "text/plain", "Alternar andando para trás.");
  });

  server.begin();

}

void loop() {}