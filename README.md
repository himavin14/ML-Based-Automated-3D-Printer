# ML-Based-Automated-3D-Printer
Automated 3D printer monitoring and image capture using Python, OpenCV and Raspberry Pi GPIO

# Project Overview:
This project aims to automate the monitoring of 3D printer by capturing images of the printed output using multiple cameras and using machine learning to analyze print quality and optimize printing parameters.

# Current Implementation
- Captures images simultaneously from three USB cameras using OpenCV.
- Uses Raspberry Pi GPIO to control an LED indicator.
- Flashes the LED after successful image capture from all three cameras.
- Saves captured images for further analysis and machine learning.

# Technologies Used
- Python
- OpenCV
- Raspberry Pi GPIO
- USB Cameras
- Machine Learning

# Future Development
- Develop a machine learning model to evaluate 3D print quality.
- Analyze the relationship between printing parameters and output quality.
- Develop predictive models to optimize print speed, feed rate and nozzle temperature.
- Integrate automated parameter adjustment based on model predictions.
