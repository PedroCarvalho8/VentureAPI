#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>

int pin1_1 = 16;
int pin1_2 = 17;
int pin1_3 = 18;
int pin1_4 = 19;

int pin2_1 = 20;
int pin2_2 = 21;
int pin2_3 = 22;
int pin2_4 = 23;

const char* ssid = "Venture";
const char* password = "321654";

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


  server.begin();
  WiFi.begin(ssid, password);

  server.on("/frente", HTTP_GET, [](AsyncWebServerRequest * request) {
    alternar_frente();
    request->send(200, "text/plain", "Alternar andando para frente.");
  });

  server.on("/tras", HTTP_GET, [](AsyncWebServerRequest * request) {
    alternar_tras();
    request->send(200, "text/plain", "Alternar andando para trás.");
  });

}

void loop() {}
