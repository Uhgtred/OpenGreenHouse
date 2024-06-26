#include <Grove_Temperature_And_Humidity_Sensor.h>
#include <ArduinoJson.h>
#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();
// #define DHTTYPE DHT22   // DHT 22  (AM2302)
// #define DHTPIN A0     // what pin we're connected to
// DHT dht(DHTPIN, DHTTYPE);

void setup() {
    /*
    Method for setting up any connections! 
    */
    Serial.begin(115200);
    // initializing i2c-connection with sht31 sensor
    if (! sht31.begin(0x44)) {   
      Serial.println("Couldn't find SHT31");
    }
    // dht.begin(); # has to be activated if dht22 shall be used (Not recommended! Guessing the humidity is as precise as this sensor.)
    // Todo: receive a setup-message from the Serial-connection which contains at least the information about the frequency with which the bus shall be read!
}


// const int tempHumiditySensorSize = 1;
const int humiditySensorSize = 1;
const int temperatureSensorSize = 1;
const int soilMoistureSize = 5;
// int tempHumiditySensors[tempHumiditySensorSize] = {A0};
int humiditySensors[humiditySensorSize] = {0x44};
int temperatureSensors[temperatureSensorSize] = {0x44};
int soilMoistureSensors[soilMoistureSensorSize] = {A1, A2, A3, A4, A5};

// struct tempHumidityData{
//     float temp, humidity;
// };

void loop() {
    /*
    Main loop, running all code that shall frequently be executed.
    */
    //if some defined message has been sent, send back sensor-Readings.
    String serialMessage;
    // skipping the mainloop if no content on the bus!
//     if (Serial.available() <= 0):
//         return;
//     serialMessage = Serial.read();
//     if (serialMessage == '1'){
        main();
//     }
    delay(5);
}

void main(){
    /*
    Main method for coordinating the system-behaviour!
    */
    DynamicJsonDocument sensorValuesJson(100);
    DynamicJsonDocument *documentPointer = &sensorValuesJson;

//     struct tempHumidityData tempHumidityValues[tempHumiditySensorSize];
    float temperatureValues[temperatureSensorSize];
    float humidityValues[humiditySensorSize];
    float soilMoistureValues[soilMoistureSize];

    iterateSensors(temperatureValues, temperatureSensors, temperatureSensorSize, &readSHT31Temperature);
    iterateSensors(humidityValues, humiditySensors, humiditySensorSize, &readSHT31Humidity);
    iterateSensors(soilMoisture, soilMoistureSensors, soilMoistureSensorSize, &readSoilMoisture);

    addJsonArray(documentPointer, "temperature", *temperatureValues, temperatureSensorSize);
    addJsonArray(documentPointer, "humidity", *humidityValues, humiditySensorSize);
    addJsonArray(documentPointer, "soilMoisture", *soilMoistureValues, soilMoistureSensorSize);

//     iterateTempHumiditySensors(tempHumidityValues, tempHumiditySensors, tempHumiditySensorSize);
//     addJsonTempHumidityValue(documentPointer, "tempHumidity", *tempHumidityValues, tempHumiditySensorSize);
//     iterateSoilMoistureSensors(soilMoistureValues, soilMoistureSensors, soilMoistureSize);
//     addJsonArray(documentPointer, "soilMoisture", soilMoistureValues, soilMoistureSize);

    sendJsonBySerial(documentPointer);
    Serial.println();
}

// void iterateSoilMoistureSensors(float *dataArray, int *pinArray, int arraySize){
//     /*
//     Method for iteratively reading sensors of same type.
//     :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
//     :param arraySize: Number of sensors that will be read.
//     */
//     for (int pinCounter=0; pinCounter<arraySize; pinCounter++){
//         int data;
//         data = readSoilMoisture(pinArray[pinCounter]);
//         dataArray[pinCounter] = data;
//     }
// }

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

void iterateTempHumiditySensors(struct tempHumidityData *dataArray, int *pinArray, int arraySize){
    /*
    Method for iteratively reading sensors of same type.
    :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
    :param arraySize: Number of sensors that will be read.
    */
    for (int pinCounter=0; pinCounter<arraySize; pinCounter++){
        struct tempHumidityData data;
        data = readSHT31(pinArray[pinCounter]);
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

// void addJsonTempHumidityValue(DynamicJsonDocument *jsonDoc, String name, struct tempHumidityData sensorStruct , int arraySize){
//     /*
//     Method for adding an array to a json-document.
//     :param jsonDoc: json-document, that the array will be stored in.
//     :param name: key of the array inside the json-document.
//     :param sensorValues: Array of sensor-values that is being stored as value to the specified key.
//     :param arraySize: Number of values that are going to be stored inside the json-document.
//     */
//     DynamicJsonDocument innerDocument(50);
//     JsonArray baseArray = innerDocument.createNestedArray(name);
//     JsonObject jsonObject = baseArray.createNestedObject();
//     jsonObject["temperature"] = sensorStruct.temp;
//     jsonObject["humidity"] = sensorStruct.humidity;
//     jsonDoc->add(innerDocument);
// }

// tempHumidityData readSHT31(int address){
//     /*
//     Todo: Reading from a specified address is currently not supported. This means that reading multiple SHT31 is curently not supported neither.
//     Method for reading a SHT31-sensor
//     :param pin: unused for the moment. Maybe there will be the possibility to read from multiple sensors later.
//     :return: The raw values <tempHumidityData> read from the sensor.
//     */
//     struct tempHumidityData sensorData;
//     sensorData.temp = sht31.readTemperature();
//     sensorData.humidity = sht31.readHumidity();
//     return sensorData;
// }

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

// tempHumidityData readDHT22(){
//     /*
//     Method for reading a DHT22-sensor. 
//     (Not recommended! That sensor-precision is shit! If possible take an SHT31 instead. That sensor seems to be much more reliable according to my testing).
//     :return: The raw-values <int> read from the sensor.
//     */
//     struct tempHumidityData sensorData;
//     float sensorValueArray[2];
//     dht.readTempAndHumidity(sensorValueArray);
//     sensorData.temp = sensorValueArray[0];
//     sensorData.humidity = sensorValueArray[1];
//     return sensorData;
// }

int readSoilMoisture(int pin){
    /*
    Reading from a given soilMoisture-Sensor
    :param pin: Analog-pin that the sensor is connected to.
    :return: The raw-values <float> read from the sensor.
    */
    return analogRead(pin);
}