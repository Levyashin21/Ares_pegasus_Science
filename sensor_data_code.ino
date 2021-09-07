/*this cade was written by Harshit Batra As the part Ares Pegasus 1.0 
 following the code reading sensor data from Pegasus rover in the following order 

  1 Temperature Using  BMP180 
  2 Pressure Using  BMP180
  3 luminosity Using BH1750
  4 Soil moisture using Capacitve Soil Sensor 
  5 Ammonia using MiCS-6814
  6 


  libraray used 
  Adafruit_BMP085.h - https://github.com/adafruit/Adafruit-BMP085-Library 
  BH1750.h - https://github.com/claws/BH1750
  
 
 */
#include <Wire.h>
#include <Adafruit_BMP085.h> 
#include <BH1750.h>
#include <gravity_soil_moisture_sensor.h>

// creating object from Adafruit_BMP085.h

Adafruit_BMP085 bmp; 

//Creating object from BH170.h

BH1750 lightMeter;

//Creating object from BH170.h

GravitySoilMoistureSensor moisture_sensor ;


void setup() {
  
  // 9600 baud rate for serial data communication
  
  Serial.begin(9600); 
  bmp .begin();
   
  // verfing BMP180's connection
   
  if (!bmp.begin()) {
    Serial.println("BMP180 NOT found");
  }
  Wire.begin();
  lightMeter.begin();
  
  // verfing BH1750's connection
   
  if (!lightMeter.begin()){
     Serial.println("BH1750 NOT found");
  }
}
void loop() {
  Serial.print("Temperature = "); 
  Serial.println(bmp.readTemperature());
  delay(10);
  Serial.print("Pressure = "); 
  Serial.println(bmp.readPressure());
  delay(10); 
  Serial.print("luminosity = ");
  Serial.println(lightMeter.readLightLevel());
  
  
  
  delay (100); 
}
