#include "Grove_Temperature_And_Humidity_Sensor.h"

#define DHTTYPE DHT22   // DHT 22  (AM2302)

/*Notice: The DHT10 and DHT20 is different from other DHT* sensor ,it uses i2c interface rather than one wire*/
/*So it doesn't require a pin.*/
#define DHTPIN A1     // what pin we're connected to（DHT10 and DHT20 don't need define it）
DHT dht(DHTPIN, DHTTYPE);   //   DHT11 DHT21 DHT22

// Connect pin 1 (on the left) of the sensor to +5V
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor if not already installed on the board.


#if defined(ARDUINO_ARCH_AVR)
    #define debug  Serial

#elif defined(ARDUINO_ARCH_SAMD) ||  defined(ARDUINO_ARCH_SAM)
    #define debug  SerialUSB
#else
    #define debug  Serial
#endif

void setup() {

    debug.begin(115200);
    Wire.begin();

    /*if using WIO link,must pull up the power pin.*/
    // pinMode(PIN_GROVE_POWER, OUTPUT);
    // digitalWrite(PIN_GROVE_POWER, 1);

    dht.begin();
}

void loop() {
    float* tempHumidityValues;
    int soilMoisture = 0;
    tempHumidityValues = readDHT22(DHTPIN);
    int rawSoilMoisture = readSoilMoisture(A2);
    // Note to myself A1 seems to have a defect!
    soilMoisture = scaleSoilMoistureValues(rawSoilMoisture);
    Serial.println(String(tempHumidityValues[0]) + "%, " + String(tempHumidityValues[1]) + "C");
    Serial.println(soilMoisture);
    delay(1500);
}

float *readDHT22(int pin){
  static float sensorValues[2] = {0};
  Serial.println(String(sensorValues[0]));
  dht.readTempAndHumidity(sensorValues);
  return sensorValues;
}

int scaleSoilMoistureValues(int rawSensorValue){
  const int moistValue = 318; // This value shall be the value of your sensor in pure water
  const int dryValue = 604; // This value shall be the value of your sensor in air.
  int scaledValue = map(rawSensorValue, moistValue, dryValue, 100, 0);
  return scaledValue;
}

int readSoilMoisture(int pin){
  float sensorValue = 0;
  return analogRead(pin);
}
