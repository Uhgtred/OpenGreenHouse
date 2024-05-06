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

const int tempHumiditySensorSize = 1;
int tempHumiditySensors[tempHumiditySensorSize] = {A0};
const int soilMoistureSize = 5;
int soilMoistureSensors[soilMoistureSize] = {A1, A2, A3, A4, A5};

float sensorValues[2] = {0, 0};

struct tempHumidityData{
    float temp, humidity;
};

void loop() {
    DynamicJsonDocument sensorValuesJson(100);
    DynamicJsonDocument *documentPointer = &sensorValuesJson;

    struct tempHumidityData tempHumidityValues[tempHumiditySensorSize];
    float soilMoistureValues[soilMoistureSize];

    iterateTempHumiditySensors(tempHumidityValues, tempHumiditySensors, tempHumiditySensorSize);
    addJsonArray(documentPointer, "tempHumidity", tempHumidityValues, tempHumiditySensorSize);
    iterateSoilMoistureSensors(soilMoistureValues, soilMoistureSensors, soilMoistureSize);
    addJsonArray(documentPointer, "soilMoisture", soilMoistureValues, soilMoistureSize);

    sendJsonBySerial(documentPointer);
    Serial.println();
    delay(1500);
}

void iterateSoilMoistureSensors(float *dataArray, int *pinArray, int arraySize){
    /*
    Method for iteratively reading sensors of same type.
    :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
    :param arraySize: Number of sensors that will be read.
    */
    for (int pinCounter=0; pinCounter<arraySize; pinCounter++){
        int data;
        data = readSoilMoisture(pinArray[pinCounter]);
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
        data = readDHT22(pinArray[pinCounter]);
        dataArray[pinCounter] = data;
    }
}

void sendJsonBySerial(DynamicJsonDocument *jsonDoc){
    /*
    Method for serializing a json-document. This is needed for sending the json-document via bus.
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
    JsonArray jsonArray = jsonDoc->createNestedArray(name);
    for(int counter = 0; counter < arraySize; counter++){
        jsonArray.add(sensorValues[counter]);
    }
}

tempHumidityData readDHT22(){
    /*
    Method for reading a DHT22-sensor (Not recommended! That sensor-precision is shit!).
    :return: The raw-values <int> read from the sensor.
    */
    struct tempHumidityData sensorData;
    float sensorValueArray[2];
    dht.readTempAndHumidity(sensorValueArray);
    sensorData.temp = sensorValueArray[0];
    sensorData.humidity = sensorValueArray[1];
    return sensorData;
}

int readSoilMoisture(int pin){
    /*
    Reading from a given soilMoisture-Sensor
    :param pin: Analog-pin that the sensor is connected to.
    :return: The raw-values <float> read from the sensor.
    */
    return analogRead(pin);
}