#include <Grove_Temperature_And_Humidity_Sensor.h>
#include <ArduinoJson.h>

#define DHTTYPE DHT22   // DHT 22  (AM2302)

/*Notice: The DHT10 and DHT20 is different from other DHT* sensor ,it uses i2c interface rather than one wire*/
/*So it doesn't require a pin.*/
#define DHTPIN A0     // what pin we're connected to（DHT10 and DHT20 don't need define it）
DHT dht(DHTPIN, DHTTYPE);   //   DHT11 DHT21 DHT22

// Connect pin 1 (on the left) of the sensor to +5V
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor if not already installed on the board.

void setup() {

    Serial.begin(115200);
    Wire.begin();

    /*if using WIO link,must pull up the power pin.*/
    // pinMode(PIN_GROVE_POWER, OUTPUT);
    // digitalWrite(PIN_GROVE_POWER, 1);

    dht.begin();
}

void loop() {
    /*
    This is the mainloop running all the code, that shall permanently be executed. 
    The frequency of the main-loop is roughly the reciprocal of the delay at the end of the loop.
    */
    // float pointer to the values which are being received from the temp-humidity-sensor.
    DynamicJsonDocument sensorValuesJson(100);
    DynamicJsonDocument *documentPointer = &sensorValuesJson;
    float* tempHumidityValues;
    tempHumidityValues = readDHT22(DHTPIN);
    int arraySize = sizeof(tempHumidityValues);
    sensorValuesJson = addJsonArray(sensorValuesJson, "TempHumid", tempHumidityValues, arraySize);
    int rawSoilMoisture = readSoilMoisture(A2);
    sensorValuesJson = addJsonFloat(sensorValuesJson, "SoilMoisture", rawSoilMoisture);
    int rawSoilMoisture2 = readSoilMoisture(A3);
    sensorValuesJson = addJsonFloat(sensorValuesJson, "SoilMoisture", rawSoilMoisture2);
    sendJsonBySerial(sensorValuesJson);
    Serial.println();
    delay(1500);
}

void sendJsonBySerial(DynamicJsonDocument jsonDoc){
    serializeJson(jsonDoc, Serial);
}

DynamicJsonDocument addJsonFloat(DynamicJsonDocument jsonDoc, String name, float sensorValue){
    if (jsonDoc.containsKey(name)){
        JsonArray jsonArray = jsonDoc[name].as<JsonArray>();
        jsonArray.add(sensorValue);
    }
    else{
        JsonArray jsonArray = jsonDoc.createNestedArray(name);
        jsonArray.add(sensorValue);
    }
    return jsonDoc;
}

DynamicJsonDocument addJsonArray(DynamicJsonDocument jsonDoc, String name, float *sensorValues, int arraySize){
    JsonArray jsonArray = jsonDoc.createNestedArray(name);
    for(int counter = 0; counter < arraySize; counter++){
        jsonArray.add(sensorValues[counter]);
    }
    return jsonDoc;
}

float *readDHT22(int pin){
  static float sensorValues[2] = {0};
//   Serial.println(String(sensorValues[0]));
  dht.readTempAndHumidity(sensorValues);
  return sensorValues;
}

float readSoilMoisture(int pin){
  /*
  Reading from a given soilMoisture-Sensor
  returning the raw-values <float>
  */
  float sensorValue = 0;
  return analogRead(pin);
}
