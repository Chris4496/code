#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <SPI.h>
#include <SD.h>
#include "RTClib.h"

// assigning pin position
#define MWSensor 3
#define DHTPIN 2

// declaring objects
RTC_DS1307 rtc;
DHT dht11 = DHT(DHTPIN, DHT11); // temperature and humidity sensor
File myData;

void setup() {
  pinMode(MWSensor,INPUT); // Microwave sensor
  Serial.begin(9600);

  // SD card initialization
  Serial.print("Initializing SD card...");
  if (!SD.begin(10)) {
  Serial.println("initialization failed!");
  while (1);
  }
  Serial.println("initialization done.");

  // Temperature and humidity initialization
  dht11.begin();

  // Real time clock initialization
  if (! rtc.begin()) {
    Serial.println("Couldn't find RTC");
    Serial.flush();
    abort();
  }
  if (! rtc.isrunning()) {
    Serial.println("RTC is NOT running, let's set the time!");
    // When time needs to be set on a new device, or after a power loss, the
    // following line sets the RTC to the date & time this sketch was compiled
    rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
    // This line sets the RTC with an explicit date & time, for example to set
    // January 21, 2014 at 3am you would call:
    // rtc.adjust(DateTime(2014, 1, 21, 3, 0, 0));
}}

void loop() {
  delay(1000);

  // open file on SD card in write mode
  myData = SD.open("test.txt", FILE_WRITE);


  // Read the humidity in %:
  float h1 = dht11.readHumidity();
  // Read the temperature as Celsius:
  float t1 = dht11.readTemperature();

  // Check if any reads failed
  if (isnan(h1) || isnan(t1)) {
    Serial.println("Failed to read from DHT11 sensor!");
    myData.println("Failed to read from DHT11 sensor!");
    return;
  }

  // Read microwave sensor
  bool Detection = digitalRead(MWSensor);

  // Read time 
  DateTime now = rtc.now();

  //---------------------------------------
  // Print time on serial
  Serial.print('[');
  Serial.print(now.year(), DEC);
  Serial.print('/');
  Serial.print(now.month(), DEC);
  Serial.print('/');
  Serial.print(now.day(), DEC);
  Serial.print(' ');
  Serial.print(now.hour(), DEC);
  Serial.print(':');
  Serial.print(now.minute(), DEC);
  Serial.print(':');
  Serial.print(now.second(), DEC);
  Serial.print(']');
  Serial.println();
  
  // print time on myData file
  myData.print('[');
  myData.print(now.year(), DEC);
  myData.print('/');
  myData.print(now.month(), DEC);
  myData.print('/');
  myData.print(now.day(), DEC);
  myData.print(' ');
  myData.print(now.hour(), DEC);
  myData.print(':');
  myData.print(now.minute(), DEC);
  myData.print(':');
  myData.print(now.second(), DEC);
  myData.print(']');
  myData.println();
  //---------------------------------------

  
  //---------------------------------------
  // print temperature and humidity on serial
  Serial.print("[DHT11]");
  Serial.print("Humidity: ");
  Serial.print(h1);
  Serial.print(" % ");
  Serial.print("Temperature: ");
  Serial.print(t1);
  Serial.print(" \xC2\xB0");
  Serial.print("C | \n");

  // print temperature and humidity on myData file
  myData.print("[DHT11]");
  myData.print("Humidity: ");
  myData.print(h1);
  myData.print(" % ");
  myData.print("Temperature: ");
  myData.print(t1);
  myData.print(" C | \n");
  //---------------------------------------


  //---------------------------------------
  // print detection result to serial and myData file
  if(Detection == HIGH){
  Serial.println("Motion detected !!\n");
  myData.print("Motion detected !!\n");}
  if(Detection == LOW){
  Serial.println("Clear\n");
  myData.print("Clear\n");}
  myData.println("\n");
  //---------------------------------------

  // close file
  myData.close();

  /* POST data to web using HTTP request
   * ........................
   * ........................
   */
  
  }
