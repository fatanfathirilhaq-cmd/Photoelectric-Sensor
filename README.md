# Through-Beam Photoelectric Sensor Speed Simulation
this project simulates a speed sensor based on the operating principle of a through-beam photoelectric sensor.

## Key Features
- Two laser sensors define the start points (initial) and end points (final).
- The object moves horizontally and returns to its starting position after leaving the screen.
- Adjustable object speed.
- Time history is recorded.

## How It Works
### Detection logic
- Only the laser beams and the object are shown on the screen. A laser beam that reaches the edge of the screen is assumed to have reached the detector.
- When the laser beam reaches the detector, the sensor state is True.
- When the laser beam does not reach the detector, the sensor become False, indicating that an object is blocking the beam. 

### Object And Sensor interaction
- The moving object is represented as a red circle whose speed can be set to any integer or decimal value.
- Interaction is detected by comparing the horizontal position of the object with the horizontal position of each sensor. When they match, an interaction occurs. 
- When a sensor interacts with the object, its laser stops at the object's and radius. In the other words, it stay directly above the object instead of reaching the detector, causing the sensor become False. 

### Recording sensor state changes:
- Once a sensor becomes False, the timestamp of the first False reading is recorded and shown on the interface.
- To prepare for future graphing features. I created a llist containing two nested lists to store the first False time and the first True time.

### Storage logic
- If the sensor is False and the first nested list is empty, the first nested list is empty. 
- If the sensor is True and the first nested list already contains data, the second nested list is filled, while a new list containing two empty nested list is inserted at the beginning of the main list so it can be filled later.

### Displaying the value
- If the sensor is False, the interface displays the first nested list.
- If the sensor is True, the interface displays the second nested list.

### Speed Calculation
- Subtract the time recorded by Sensor 1 from the time recorded by Sensor 2 to obtain the time interval.
- Subtract the position of Sensor 1 from the position of Sensor 2 to obtain the distance.
- Substitute the previously calculated values into the speed formula :
```
speed = distance / time 
```

## Requirement 
- Python 3.13+
- Numpy
- Pygame

## Installation
``` 
git clone 
cd ".\Photoelectric Sensor"
pip install numpy pygame
python main.py
```
