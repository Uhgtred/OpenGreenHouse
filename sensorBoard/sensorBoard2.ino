#include <Grove_Temperature_And_Humidity_Sensor.h>
#include <ArduinoJson.h>

#define DHTTYPE DHT22   // DHT 22  (AM2302)
#define DHTPIN A0     // what pin we're connected to
DHT dht(DHTPIN, DHTTYPE);

void setup() {
    Serial.begin(115200);
    Wire.begin();
    dht.begin();
}

void loop() {
    DynamicJsonDocument sensorValuesJson(100);
    DynamicJsonDocument *documentPointer = &sensorValuesJson;

    int tempHumidityPins[1] = {A0};
    int soilMoisturePins[5] = {A1, A2, A3, A4, A5};

    float tempHumidityValues[sizeof(tempHumidityPins)/sizeof(tempHumidityPins[0])];
    float soilMoistureData[sizeof(soilMoisturePins)/sizeof(soilMoisturePins[0])];

    iterateSensorsOfType(tempHumidityValues, sizeof(tempHumidityPins)/sizeof(tempHumidityPins[0]), readDHT22);
    iterateSensorsOfType(soilMoistureData, sizeof(soilMoisturePins)/sizeof(soilMoisturePins[0]), readSoilMoisture);

    sendJsonBySerial(sensorValuesJson);
    Serial.println();
    delay(1500); 
}

/* Method for iteratively reading sensors of same type.
* :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
* :param arraySize: Number of sensors that will be read.
* :param (*func): Method that will read a sensor.
*/
void iterateSensorsOfType(float *dataArray, int arraySize, float (*func)(int)){
    for (int pinCounter=0; pinCounter<arraySize; pinCounter++){
        float data;
        data = func(pinCounter + 1);
        dataArray[pinCounter] = data;
    }
}

/* Method for serializing a json-document. This is needed for sending the json-document via bus.
* This will be done by reference. So there is no return-value.
* :param jsonDoc: json-document that will be serialized.
*/
void sendJsonBySerial(DynamicJsonDocument jsonDoc){
    serializeJson(jsonDoc, Serial);
}

/* Method for adding a float-value to a json-document.
* :param jsonDoc: json-document, that the array will be stored in.
* :param name: key of the array inside the json-document.
* :param sensorValue: Single sensor-value that is being stored to the specified key.
*/
DynamicJsonDocument addJsonFloat(DynamicJsonDocument jsonDoc, String name, float sensorValue){
    if (jsonDoc.containsKey(name)){
        JsonArray jsonArray = jsonDoc[name].as<JsonArray>();
        jsonArray.add(sensorValue);
    } else {
        JsonArray jsonArray = jsonDoc.createNestedArray(name);
        jsonArray.add(sensorValue);
    }
    return jsonDoc;
}

/* Method for adding an array to a json-document.
* :param jsonDoc: json-document, that the array will be stored in.
* :param name: key of the array inside the json-document.
* :param sensorValues: Array of sensor-values that is being stored as value to the specified key.
* :param arraySize: Number of values that are going to be stored inside the json-document.
*/
DynamicJsonDocument addJsonArray(DynamicJsonDocument jsonDoc, String name, float *sensorValues, int arraySize){
    JsonArray jsonArray = jsonDoc.createNestedArray(name);
    for(int counter = 0; counter < arraySize; counter++){
        jsonArray.add(sensorValues[counter]);
    }
    return jsonDoc;
}

/* Method for reading a DHT22-sensor (Not recommended! That sensor-precision is shit!).
* :param pin: Analog-pin that the sensor is connected to.
* :return: The raw-values <float> read from the sensor.
*/
float readDHT22(int pin){
    float sensorValues = 0; // Placeholder value. Replace with actual values read from the sensor.
    return sensorValues;
}

/*
* Reading from a given soilMoisture-Sensor
* :param pin: Analog-pin that the sensor is connected to.
* :return: The raw-values <float> read from the sensor.
*/
float readSoilMoisture(int pin){
    float sensorValue = 0; // Placeholder. Replace with actual value read from sensor.
    return sensorValue;
}