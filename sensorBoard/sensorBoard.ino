#include <Grove_Temperature_And_Humidity_Sensor.h>
#include <ArduinoJson.h>
#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();

void setup() {
    /*
    Method for setting up any connections! 
    */
    Serial.begin(115200);
    // initializing i2c-connection with sht31 sensor
    if (! sht31.begin(0x44)) {   
      Serial.println("Couldn't find SHT31");
    }
}


const int humiditySensorSize = 1;
const int temperatureSensorSize = 1;
const int soilMoistureSize = 5;
int humiditySensors[humiditySensorSize] = {0x44};
int temperatureSensors[temperatureSensorSize] = {0x44};
int soilMoistureSensors[soilMoistureSensorSize] = {A1, A2, A3, A4, A5};


void loop() {
    /*
    Main loop, running all code that shall frequently be executed.
    */
    DynamicJsonDocument<80> serialMessageJson;
    serialMessageJson = readSerialJson(serialMessageJson);
    int jsonData;
    jsonData = readJsonValue("TransmitSensorData");
    if (jsonData = 1){
        main();
    }
    delay(5);
}

DynamicJsonDocument readSerialJson(DynamicJsonDocument serialMessageJson){
    if (Serial.available()){
        String jsonData = Serial.readStringUntil('&');
        // storing jsonData into global json document
        deserializeJson(serialMessageJson, jsonData);
        return serialMessageJson;
    }
}

void main(){
    /*
    Main method for coordinating the system-behaviour!
    */
    DynamicJsonDocument sensorValuesJson(100);
    DynamicJsonDocument *documentPointer = &sensorValuesJson;

    float temperatureValues[temperatureSensorSize];
    float humidityValues[humiditySensorSize];
    float soilMoistureValues[soilMoistureSize];

    iterateSensors(temperatureValues, temperatureSensors, temperatureSensorSize, &readSHT31Temperature);
    iterateSensors(humidityValues, humiditySensors, humiditySensorSize, &readSHT31Humidity);
    iterateSensors(soilMoisture, soilMoistureSensors, soilMoistureSensorSize, &readSoilMoisture);

    addJsonArray(documentPointer, "temperature", *temperatureValues, temperatureSensorSize);
    addJsonArray(documentPointer, "humidity", *humidityValues, humiditySensorSize);
    addJsonArray(documentPointer, "soilMoisture", *soilMoistureValues, soilMoistureSensorSize);

    sendJsonBySerial(documentPointer);
    Serial.println();
}

int readJsonValue(String key){
    int value = jsonDocument[key];
    return value;
}

void iterateSensors(float *dataArray, int *pinArray, int arraySize, (*function)(int){
    /*
    Method for iteratively reading sensors of same type.
    :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
    :param arraySize: Number of sensors that will be read.
    */
    for (int pinCounter=0; pinCounter<arraySize; pinCounter++){
        float data;
        data = function(pinArray[pinCounter]);
        dataArray[pinCounter] = data;
    }
}

void sendJsonBySerial(DynamicJsonDocument *jsonDoc){
    /*
    Method for serializing and sending a json-document. This is needed for sending the json-document via bus.
    This will be done by reference. So there is no return-value.
    :param jsonDoc: json-document that will be serialized.
    */
    serializeJson(*jsonDoc, Serial);
}

void addJsonArray(DynamicJsonDocument *jsonDoc, String name, float *sensorValues, int arraySize){
    /*
    Method for adding an array to a json-document.
    :param jsonDoc: json-document, that the array will be stored in.
    :param name: key of the array inside the json-document.
    :param sensorValues: Array of sensor-values that is being stored as value to the specified key.
    :param arraySize: Number of values that are going to be stored inside the json-document.
    */
    DynamicJsonDocument innerDocument(50);
    JsonArray innerArray = innerDocument.createNestedArray(name);
    JsonObject soilMoistureObject = innerDocument.createNestedObject();
    for(int counter = 0; counter < arraySize; counter++){
        innerArray.add(sensorValues[counter]);
    }
    jsonDoc->add(innerDocument);
}

float readSHT31Temperature(int address){
    sht31.begin(address);
    float temperature;
    temperature = sht31.readTemperature();
    return temperature;
}

float readSHT31Humidity(int address){
    sht31.begin(address);
    float humidity;
    humidity = sht31.readHumidity();
    return humidity;
}

int readSoilMoisture(int pin){
    /*
    Reading from a given soilMoisture-Sensor
    :param pin: Analog-pin that the sensor is connected to.
    :return: The raw-values <float> read from the sensor.
    */
    return analogRead(pin);
}