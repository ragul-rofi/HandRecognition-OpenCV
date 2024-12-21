
# Hand Gesture Recognition using OpenCV

This project uses OpenCV to recognize hand gestures in real-time via a webcam. The program detects the hand and counts the number of fingers raised based on the convexity defects in the hand contour.

## Features

- Real-time hand gesture recognition using webcam.
- Detects the number of fingers raised.
- Uses convexity defects for finger detection.
- Works on most webcams.

## Requirements

To run this project, you will need to install the following Python libraries:

- **OpenCV**: For image processing and computer vision tasks.
- **NumPy**: For numerical operations (specifically for vector math).

You can install these libraries using pip:

```bash
pip install opencv-python opencv-python-headless numpy
```

## Project Structure

The project consists of a single Python script:

- **main.py**: The main script that captures webcam feed, processes the image, detects hand contours, and counts the number of fingers.

## How to Run

1. Ensure that you have Python 3.x installed on your machine.
2. Install the required libraries by running the command:
   ```bash
   pip install opencv-python opencv-python-headless numpy
   ```
3. Clone or download the project.
4. Open a terminal or command prompt and navigate to the directory containing `main.py`.
5. Run the script:
   ```bash
   python main.py
   ```
6. A window will appear showing the webcam feed with hand gesture recognition. The program will print the number of fingers detected in the console.
7. To exit the program, press the `q` key.

## How It Works

1. **Webcam Feed**: The script opens a webcam stream using OpenCV.
2. **Preprocessing**: The webcam frames are converted to grayscale and blurred to reduce noise. A binary threshold is applied to isolate the hand from the background.
3. **Contour Detection**: The contours of the thresholded image are found, and the largest contour (assumed to be the hand) is selected.
4. **Convexity Defects**: The convexity defects of the hand contour are calculated to identify the finger separations.
5. **Angle Calculation**: For each defect, the angle between the points is calculated using vector math. If the angle is less than 90 degrees, it is considered a finger.
6. **Depth Filtering**: The defect depth is used to filter out shallow indentations and false positives.
7. **Finger Count**: The number of fingers is counted based on the detected convexity defects.


## Future Improvements

- Improve finger detection accuracy for more complex gestures.
- Add gesture-based control to interact with the computer (e.g., mouse control).
- Implement a model to recognize different hand gestures for control purposes.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.
