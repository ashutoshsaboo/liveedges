# Live Edges

This project takes a live recording using your webcam/feed a video as an input, and then makes a mask to differentiate, the regions having white colors, and then detects edges of the white colored object. 

<a href="https://en.wikipedia.org/wiki/Canny_edge_detector">Canny Edge Detection</a> Algorithm is used to detect live edges. 

## Project Dependencies-:

1. OpenCV `cv2` Library for Python - http://opencv.org/
2. NumPy - www.numpy.org

It's better to install the above dependencies in Virtual Environment `virtualenv`.

## Files Description-:

1. `tracklivewhite.py` - Records a live video, using the webcam, and then the script tracks the white object with it's edges.`

2. `trackwhite.py` - User needs to feed a video as an input, and then the script tracks the white object with it's edges.

## Credits-:

Ashutosh Saboo - https://github.com/ashutoshsaboo - https://github.com/ashutoshsaboo/liveedges

