# Requirements

---
## Table of Contents
### (GUI)[#gui]
### (Sensors)[#sensors]

---
## Gui
The Application shall have an Api that provides information about the things that are to be displayed.
The GUI shall be useable locally through a touchscreen and from a webbrowser, so the user is able to set and receive 
data through a mobile device on the network (maybe internet?).

---
## Sensors
Each Sensor that is to be read has to have a type-specific id. Type-specific means, that a soilmoisture-sensor can have 
the same id as a humidity-sensor, because they are different sensor-types. With that id it has to be possible to set a 
specific deviation for each sensor, so that each sensor can be calibrated. The calibrated sensor-values shall be shown 
in a user-interface and both the calibrated and the uncalibrated values shall be stored in a database.
The user has to define how many sensors of a type are connected.