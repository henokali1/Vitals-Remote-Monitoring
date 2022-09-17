void tempSetup(){
  if (therm.begin() == false){ // Initialize thermal IR sensor
    Serial.println("Qwiic IR thermometer did not acknowledge! Freezing!");
    while(1);
  }
  Serial.println("Qwiic IR Thermometer did acknowledge.");
  
  therm.setUnit(TEMP_C); // Set the library's units to Farenheit
  // Alternatively, TEMP_F can be replaced with TEMP_C for Celsius or
  // TEMP_K for Kelvin.
  
  pinMode(LED_BUILTIN, OUTPUT); // LED pin as output
}

void bioSensorSetup(){
  int result = bioHub.begin();
  if (!result)
    Serial.println("Sensor started!");
  else
    Serial.println("Could not communicate with the sensor!!!");

  Serial.println("Configuring Sensor...."); 
  int error = bioHub.configBpm(MODE_ONE); // Configuring just the BPM settings. 
  if(!error){
    Serial.println("Sensor configured.");
  }
  else {
    Serial.println("Error configuring sensor.");
    Serial.print("Error: "); 
    Serial.println(error); 
  }
  // Data lags a bit behind the sensor, if you're finger is on the sensor when
  // it's being configured this delay will give some time for the data to catch
  // up. 
  delay(4000);   
}


void updateTemp(){
  if (therm.read()) // On success, read() will return 1, on fail 0.
  {
    // Use the object() and ambient() functions to grab the object and ambient
  // temperatures.
  // They'll be floats, calculated out to the unit you set with setUnit().
    
    ambient_temp_val = String(therm.ambient(), 2);
    if(abs(therm.object() - therm.ambient()) > 3){
      body_temp_val = String(therm.object(), 2);
    } else {
      body_temp_val = "0.0";
    }
    
//    Serial.print("Object: " + body_temp_val);
//    Serial.println("C");
//    Serial.print("Ambient: " + ambient_temp_val);
//    Serial.println("C");
//    Serial.println();
  }
}

void updateHr(){
  body = bioHub.readBpm();
  if(body.confidence > 60){
    heartrate_val = String(body.heartRate);
//    Serial.print("heartrate_val: ");
//    Serial.println(heartrate_val); 
  } else {
    heartrate_val = "0.0";
  }
}

void frmtMsg(){
  wifiMsg = "AT+NWHTC=http://54.166.105.47:9999/update_live/?heart_rate=" + heartrate_val + "&body_temp=" + body_temp_val + ",get";
  Serial.println(wifiMsg);
}
