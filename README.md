# Dangerous Writing App

## Description
The Dangerous Writing App is a unique writing tool designed to boost creativity and combat writer's block. It challenges users to keep writing continuously, or risk losing all their work if they pause for too long.

### Features

* Simple and distraction-free writing interface.
* 5-second countdown timer that resets with each keystroke.
* All text disappears if the user stops typing for 5 seconds.
* Option to save work before closing the application.

### Technologies
* Python

### Python Libs
* Tkinter

## Getting Started
1. Clone this repository.
2. Create virtual environment.
3. Run [script](main.py) in Python. 

## Usage
1. Click the "Start writing!" button to begin.
2. Start typing immediately. Remember, if you stop typing for 5 seconds, all your work will disappear!
3. To save your work, click the "Save" button. This will pause the timer and allow you to choose a location to save your file.

## Customization
* Change the countdown duration by modifying the `count_down(5)` call and related text.
* Adjust the window size by changing the `window.minsize(width=1500, height=900)` line.
* Modify the text box size by changing the `Text(height=25, width=115, ...)` parameters.
