# WorkoutTracker

The script processes inputs related to an exercise session. Upon receiving details about 
the type of training and the raw data, it will provide the following information:

1)Type of Training
2) Time Taken
3)Total Distance Covered
4) Mean Velocity
5) Calories Burned.

# App Use
- Implemented calorie computation for Swimming, Running, and Sport Walking activities.

- ## Installation (windows)

Install environment
```sh
cd module-Workout-tracker/
```
```sh
python -m venv venv
```
Activate environment
```sh
source venv/Scripts/activate
```
Install requirements
```sh
pip install -r requirements.txt
```
Run script
```sh
python Workout_tracker.py
```
## Usage
#### Input data
```sh
'SWM', [720, 1, 80, 25, 40]
```
| # | SWM | Description | units |
| - | --- | ----------- | ----- |
| 1 | 720 | numbers of strokes in swimming | ea |
| 2 | 1 | duration | h |
| 3 | 80 | weight | kg |
| 4 | 25 | pool leight | m |
| 5 | 40 | counts pool during training | ea |

#### Output data
```sh
Training type: Swimming; Duration: 1.000 h.; Distance: 0.994 m; Avg. speed: 1.000 mph; Spent cal: 336.000.
