#include <Wire.h>
#include <SparkFun_Bio_Sensor_Hub_Library.h>
#include <SparkFunMLX90614.h>
#include <SerLCD.h> 


// No other Address options.
#define DEF_ADDR 0x55

// Reset pin, MFIO pin
const int resPin = 4;
const int mfioPin = 5;

// Takes address, reset pin, and MFIO pin.
SparkFun_Bio_Sensor_Hub bioHub(resPin, mfioPin); 
IRTherm therm; // Create an IRTherm object to interact with throughout
SerLCD lcd; // Initialize the library with default I2C address 0x72


bioData body;  
String heartrate_val = "0.0";
String body_temp_val = "0.0";
String ambient_temp_val = "";
String ecg = "";
String wifiMsg = "";
void setup(){
  Serial.begin(115200);
  Wire.begin();
  tempSetup();
  bioSensorSetup();
  lcdSetup();
}

void loop(){
  updateTemp();
  updateHr();
  updateEcg();
  frmtMsg();
  updateLcd();
  delay(1000); // Slowing it down, we don't need to break our necks here.
}
