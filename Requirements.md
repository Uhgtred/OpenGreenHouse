# Requirements

---
## Table of Contents
### [GUI](#gui)
### [Sensors](#sensors)
### [Actors](#actors)
### [Grow Journal](#grow-journal)
### [Grow](#grow)
### [Database](#database)

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
## Actors
The project needs to have the possibility to control actors through the API.
This means that it needs to be possible to control, for example, a light. 
The specifics on how an actor can be controlled has to be defined in the Actor itself, since the actors will be too different to generalize the control. 

---
## Grow-journal
There needs to be a journal, in which the gardener can make notes for every day.
Also, the sensor-data shall automatically be stored inside each day of the journal, so that it is possible to track the environment of the greenhouse for every day.

---
## Grow
It shall be possible to start a new grow through the UI.
This shall trigger the backend to create a new folder. 
Inside this folder there needs to be another directory, containing a database-file for sensor-data to be stored in.
It shall be possible as well to start a manual grow or start an automated grow that uses a profile (see [Sensordata Database](#sensordata-database) to set the grow-environment automatically.)

---
## Database
There needs to be a multiple databases, as follows:
- ### Sensordata Database
    This database shall contain a table for each day of the grow.
    Inside these tables there shall be all sensor-data recorded during this day.
    Also the database shall have a unique name, referring to the plant, that will be grown. 
    That way this database can be used as a kind of profile for one specific plant (automated control of the actors according to profile).
- ### Sensor Database
  This database shall contain a table for each sensor-type that is connected (e.g.: soilMoisture, humidity, temperature).
  Those tables shall contain information about how many sensors of that type are connected, what is the sensor-id (for identification of a specific sensor) and information about the calibration of the sensor.


