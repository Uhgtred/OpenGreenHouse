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
    int tempHumidityPins[1] = {A0};
    float tempHumidityValues[sizeof(tempHumidityValues)];

    tempHumidityValues = iterateSensorsOfType(*tempHumidityValues, sizeof(soilMoisturePins, readDHT22);

//     tempHumidityValues = readDHT22(DHTPIN);
//     int arraySize = sizeof(tempHumidityValues);
//     sensorValuesJson = addJsonArray(sensorValuesJson, "TempHumid", tempHumidityValues, arraySize);

    // TODO: create an array containing all the pins that sensors could be connected to and iterate over that array using the iterateSensorsOfType-method.
    // And swap the following lines for that:
    int soilMoisturePins[5] = {A1, A2, A3, A4, A5};
    float soilMoistureData[sizeof(soilMoisturePins)];
    soilMoistureData = iterateSensorsOfType(*soilMoistureData, sizeof(soilMoisturePins), readSoilMoisture);

//     int *sensorIdAndValue[2];
//     sensorIdAndValue[0] = 1;
//     int rawSoilMoisture = readSoilMoisture(A2);
//     sensorValuesJson = addJsonFloat(sensorValuesJson, "SoilMoisture", rawSoilMoisture);
//     int rawSoilMoisture2 = readSoilMoisture(A3);
//     sensorValuesJson = addJsonFloat(sensorValuesJson, "SoilMoisture", rawSoilMoisture2);

    sendJsonBySerial(sensorValuesJson);
    Serial.println();  // finish the line with an empty line printed to the bus.
    delay(1500);  // defines the reciprocal of the read-rate.
}

float iterateSensorsOfType(int *sensorPinArray, int arraySize, float (*func)(int){
    /*
    Method for iteratively reading sensors of same type.
    :param sensorPinArray: Array containing the pin-numbers of each sensor that has to be read.
    :param arraySize: Number of sensors that will be read.
    :param (*func): Method that will read a sensor.
    */
    float dataArray[arraySize][2];
    for (int pinCounter=0; pinCounter<=arraySize; pinCounter++){
        float data[2];
        data[1] = func(sensorPinArray[pinCounter]);
        data[0] = pinCounter + 1; // This shall serve as an id for the sensor. So it shall not start at 0.
        dataArray[pinCounter] = data;
    }
    return dataArray;
}

void sendJsonBySerial(DynamicJsonDocument jsonDoc){
    /*
    Method for serializing a json-document. This is needed for sending the json-document via bus.
    This will be done by reference. So there is no return-value.
    :param jsonDoc: json-document that will be serialized.
    */
    serializeJson(jsonDoc, Serial);
}

DynamicJsonDocument addJsonFloat(DynamicJsonDocument jsonDoc, String name, float sensorValue){
    /*
    Method for adding a float-value to a json-document.
    :param jsonDoc: json-document, that the array will be stored in.
    :param name: key of the array inside the json-document.
    :param sensorValue: Single sensor-value that is being stored to the specified key.
    */
    if (jsonDoc.containsKey(name)){
        // Adding to an existing key, if it already exists inside the json-document.
        JsonArray jsonArray = jsonDoc[name].as<JsonArray>();
        jsonArray.add(sensorValue);
    }
    else{
        // Creating new nested array if the key does not yet exist inside the json-document.
        JsonArray jsonArray = jsonDoc.createNestedArray(name);
        jsonArray.add(sensorValue);
    }
    return jsonDoc;
}

DynamicJsonDocument addJsonArray(DynamicJsonDocument jsonDoc, String name, float *sensorValues, int arraySize){
    /*
    Method for adding an array to a json-document.
    :param jsonDoc: json-document, that the array will be stored in.
    :param name: key of the array inside the json-document.
    :param sensorValues: Array of sensor-values that is being stored as value to the specified key.
    :param arraySize: Number of values that are going to be stored inside the json-document.
    */
    // Creating an array inside an existing json-document with the key <name>.
    JsonArray jsonArray = jsonDoc.createNestedArray(name);
    for(int counter = 0; counter < arraySize; counter++){
        jsonArray.add(sensorValues[counter]);
    }
    return jsonDoc;
}

float *readDHT22(int pin){
    /*
    Method for reading a DHT22-sensor (Not recommended! That sensor-precision is shit!).
    :param pin: Analog-pin that the sensor is connected to.
    :return: The raw-values <float> read from the sensor.
    */
    static float sensorValues[2] = {0};
    dht.readTempAndHumidity(sensorValues);
    return sensorValues;
}

float readSoilMoisture(int pin){
  /*
  Reading from a given soilMoisture-Sensor
  :param pin: Analog-pin that the sensor is connected to.
  :return: The raw-values <float> read from the sensor.
  */
  float sensorValue = 0;
  return analogRead(pin);
}
