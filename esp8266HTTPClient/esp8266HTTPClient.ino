#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

int Sensor = 4;     // RCWL-0516 Input Pin
 
int sensorval = 0;  // RCWL-0516 Sensor Value

bool have_human = false;
 
void setup() {
 
  Serial.begin(115200);   // Serial connection   
  pinMode (Sensor, INPUT);
  
  WiFi.begin("ASUS_Guest1", "ptuoc_coutp");   // WiFi connection
 
  while (WiFi.status() != WL_CONNECTED) {  // Wait for the WiFI connection completion
 
    delay(500);
    Serial.println("Waiting for connection");
 
  }
 
}
 
void loop() {
  sensorval = digitalRead(Sensor); // Read sensor value
    
  if (sensorval == HIGH) {
    have_human = true;
      // Turn LED On
  } else {
    have_human = false;
    }
 
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
    JsonObject& JSONencoder = JSONbuffer.createObject(); 
 
    JSONencoder["location"] = "room404";

// json array example
//    JsonArray& values = JSONencoder.createNestedArray("values"); //JSON array
//    values.add(20); //Add value to array
//    values.add(21); //Add value to array
//    values.add(23); //Add value to array

    JSONencoder["human"] = (bool)have_human;
    
    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    Serial.println(JSONmessageBuffer);
 
    HTTPClient http;    //Declare object of class HTTPClient
 
    http.begin("http://192.168.1.11/postjson");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
 
    int httpCode = http.POST(JSONmessageBuffer);   //Send the request
    String payload = http.getString();                                        //Get the response payload
 
    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload
 
    http.end();  //Close connection
 
  } else {
 
    Serial.println("Error in WiFi connection");
 
  }
 
  delay(10000);  //Send a request every 30 seconds
 
}
