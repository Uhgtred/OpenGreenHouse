# Requirements

---
## Table of Contents
### [GUI](#gui)
### [Sensors](#sensors)
### [Grow Journal](#grow-journal)

---
## Gui
The Application shall have an API that provides information about the things that are to be displayed.
The GUI shall be usable locally through a touchscreen and from a browser or an app on a mobile-device or both. 
So the user is able to set and receive data through a mobile device on the network (maybe internet?).

---
## Sensors
Each Sensor that is to be read has to have a type-specific id. Type-specific means, that a soilmoisture-sensor can have 
the same id as a humidity-sensor, because they are different sensor-types. With that id it has to be possible to set a 
specific deviation for each sensor, so that each sensor can be calibrated. The calibrated sensor-values shall be shown 
in a user-interface, and both the calibrated and the uncalibrated values shall be stored in a database.
The user has to define how many sensors of a type are connected.

---
## Grow-journal
There needs to be a journal, in which the gardener can make notes for every day.
Also, the sensor-data shall automatically be stored inside each day of the journal, so that it is possible to track the environment of the greenhouse for every day.

---
